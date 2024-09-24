import omf_python
from os import path
from unittest import TestCase


class TestProjectedTextureAttribute(TestCase):
    def setUp(self) -> None:
        omf_dir = path.join(path.dirname(__file__), "data")
        one_of_everything = path.join(omf_dir, "one_of_everything.omf")
        self.reader = omf_python.Reader(one_of_everything)

        test_png = path.join(omf_dir, "test.png")
        with open(test_png, "rb") as file:
            self.image = file.read()

    def test_should_return_expected_projected_texture_attribute(self) -> None:
        projected_texture_attribute = self.reader.project.elements[9].attributes[0]
        self.assertEqual("Projected", projected_texture_attribute.name)

        attribute_data = projected_texture_attribute.get_data()

        self.assertEqual(1.0, attribute_data.width)
        self.assertEqual(1.0, attribute_data.height)

        orient = attribute_data.orient

        self.assertEqual([0.0, 0.0, 0.0], orient.origin)
        self.assertEqual([1.0, 0.0, 0.0], orient.u)
        self.assertEqual([0.0, 1.0, 0.0], orient.v)

        image = attribute_data.image

        # Images always have an item count of zero
        self.assertEqual(0, image.item_count)

        image_bytes = self.reader.image_bytes(image)
        self.assertEqual(self.image, image_bytes)
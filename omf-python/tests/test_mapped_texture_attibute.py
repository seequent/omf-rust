import omf_python
from os import path
from unittest import TestCase


class TestMappedTextureAttribute(TestCase):
    def setUp(self) -> None:
        omf_dir = path.join(path.dirname(__file__), "data")
        one_of_everything = path.join(omf_dir, "one_of_everything.omf")
        self.reader = omf_python.Reader(one_of_everything)

        test_png = path.join(omf_dir, "test.png")
        with open(test_png, "rb") as file:
            self.image = file.read()

    def test_should_return_expected_texture_attributes(self) -> None:
        # Given an element with a MappedTexture attribute
        attributes = self.reader.project.elements[9].attributes
        self.assertEqual(2, len(attributes))

        # Then should be able to get the MappedTexture attribute
        texture_attributes = [a for a in attributes if a.name == "Mapped"]
        self.assertEqual(1, len(texture_attributes))

        # And it should have texture coordinates
        texcoords = texture_attributes[0].get_data().texcoords

        # And those coordinates should match the expected value
        self.assertEqual(4, texcoords.item_count)
        coordinates = self.reader.array_texcoord(texcoords)
        self.assertEqual(4, len(coordinates))
        COORDINATES = [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]]
        self.assertEqual(COORDINATES, coordinates)

        # And it should contain an image
        image = texture_attributes[0].get_data().image
        # Images always have an item count of zero
        self.assertEqual(0, image.item_count)

        # And the image contents should match those expected
        bytes = self.reader.image_bytes(image)
        self.assertEqual(self.image, bytes)
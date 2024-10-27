from os import path
from unittest import TestCase

import omf_python


class TestLineSet(TestCase):
    def setUp(self) -> None:
        omf_dir = path.join(path.dirname(__file__), "data")
        one_of_everything = path.join(omf_dir, "one_of_everything.omf")
        self.reader = omf_python.Reader(one_of_everything)
        self.project, _ = self.reader.project()
        self.lineset = self.project.elements()[2]

    def test_should_return_expected_geometry_type(self) -> None:
        self.assertIsInstance(self.lineset.geometry(), omf_python.LineSet)

    def test_should_return_expected_origin(self) -> None:
        lineset_origin = self.lineset.geometry().origin
        self.assertEqual(lineset_origin, [0.0, 0.0, 0.0])

    def test_should_return_expected_vertices(self) -> None:
        # Given
        vertices_array = self.lineset.geometry().vertices

        # When
        vertices = self.reader.array_vertices(vertices_array)

        # Then
        expected_vertices = [
            [-1.0, -1.0, 0.0],
            [1.0, -1.0, 0.0],
            [1.0, 1.0, 0.0],
            [-1.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
        self.assertEqual(vertices, expected_vertices)

    def test_should_return_expected_segments(self) -> None:
        # Given
        segments_array = self.lineset.geometry().segments

        # When
        segments = self.reader.array_segments(segments_array)

        # Then
        expected_segments = [
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0],
            [0, 4],
            [1, 4],
            [2, 4],
            [3, 4],
        ]
        self.assertEqual(segments, expected_segments)

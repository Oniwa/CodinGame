import unittest
from MIME_Types.mime import mime_types

class TestMimeTypes(unittest.TestCase):

    def test_mime_simple(self):
        table_length = 3
        num_files = 3
        association_table = ['html text/html', 'png image/png', 'gif image/gif']
        files = ['animated.gif', 'portrait.png', 'index.html']

        result = mime_types(table_length, num_files, association_table, files)

        self.assertEqual(result[0], 'image/gif')
        self.assertEqual(result[1], 'image/png')
        self.assertEqual(result[2], 'text/html')

    def test_mime_unknown(self):
        table_length = 3
        num_files = 4
        association_table = ['txt text/plain', 'xml text/xml',
                             'flv video/x-flv']

        files = ['image.png', 'animated.gif', 'script.js', 'source.cpp']

        result = mime_types(table_length, num_files, association_table, files)

        self.assertEqual(result[0], 'UNKNOWN')
        self.assertEqual(result[1], 'UNKNOWN')
        self.assertEqual(result[2], 'UNKNOWN')
        self.assertEqual(result[3], 'UNKNOWN')

    def test_mime_correct_division_of_the_extension(self):
        table_length = 3
        num_files = 11
        association_table = ['wav audio/x-wav', 'mp3 audio/mpeg',
                             'pdf application/pdf']

        files = ['a', 'a.wav', 'b.wav.tmp', 'test.vmp3', 'pdf', '.pdf',
                 'mp3', 'report..pdf', 'defaultwav', '.mp3.', 'final.']

        result = mime_types(table_length, num_files, association_table, files)

        self.assertEqual(result[0], 'UNKNOWN')
        self.assertEqual(result[1], 'audio/x-wav')
        self.assertEqual(result[2], 'UNKNOWN')
        self.assertEqual(result[3], 'UNKNOWN')
        self.assertEqual(result[4], 'UNKNOWN')
        self.assertEqual(result[5], 'application/pdf')
        self.assertEqual(result[6], 'UNKNOWN')
        self.assertEqual(result[7], 'application/pdf')
        self.assertEqual(result[8], 'UNKNOWN')
        self.assertEqual(result[9], 'UNKNOWN')
        self.assertEqual(result[10], 'UNKNOWN')

    def test_mime_consideration_of_the_case(self):
        table_length = 4
        num_files = 7
        association_table = ['png image/png', 'TIFF image/TIFF', 'css text/css',
                             'TXT text/plain]']

        files = ['example.TXT', 'referecnce.txt', 'strangename.tiff',
                 'resolv.CSS', 'matrix.TiFF', 'lanDsCape.Png', 'extract.cSs']

        result = mime_types(table_length, num_files, association_table, files)

        self.assertEqual(result[0], 'text/plain')
        self.assertEqual(result[1], 'text/plain')
        self.assertEqual(result[2], 'image/TIFF')
        self.assertEqual(result[3], 'text/css')
        self.assertEqual(result[4], 'image/TIFF')
        self.assertEqual(result[5], 'image/png')
        self.assertEqual(result[6], 'text/css')


class TestType2Dict(unittest.TestCase):
    def test_type_to_dict(self):
        association_table = ['html text/html', 'png image/png', 'gif image/gif']

        mime_dict = type_to_dict(association_table)

        self.assertEqual(mime_dict['html'], 'text/html')
        self.assertEqual(mime_dict['png'], 'image/png')
        self.assertEqual(mime_dict['gif'], 'image/gif')

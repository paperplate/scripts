import unittest

import sys
sys.path.append('../videoEncoding')
import convertDir

testStrs = {
    'bracketAtEnd': 'Zootopia.2.2025.1080p.WEBRip.x264.AAC5.1-[YTS.BZ].mp4',
    'noBracket': 'A.Minecraft.Movie.2025.1080p.WEB.h264-ETHEL.mkv',
    'middleFile': '[Erai-raws] Dr Stone - Science Future Part 2 - 01 [1080p CR WEBRip HEVC EAC3][MultiSub][3B462F1E].mkv'
}

class TestStringMethods(unittest.TestCase):
    def test_nameInMiddle(self):
        fileName = convertDir.extractName(testStrs['middleFile'], '.mkv')
        self.assertEqual(fileName, 'Dr Stone - Science Future Part 2 - 01.mkv')

    def test_bracketAtEnd(self):
        fileName = convertDir.extractName(testStrs['bracketAtEnd'], '.mp4')
        self.assertEqual(fileName, 'Zootopia.2.2025.1080p.WEBRip.x264.AAC5.1-[YTS.BZ] (1).mp4')

    def test_noBracket(self):
        fileName = convertDir.extractName(testStrs['noBracket'], '.mkv')
        self.assertEqual(fileName, 'A.Minecraft.Movie.2025.1080p.WEB.h264-ETHEL (1).mkv')

if __name__ == '__main__':
    unittest.main()

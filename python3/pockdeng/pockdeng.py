import unittest


class DengTest(unittest.TestCase):
    def setUp(self):
        self.deng = Deng()

    def test_players_get_face_cards_should_return_0(self):
        result = self.deng.check(['KD', 'KC'])
        self.assertEqual(result, 0)

    def test_players_get_JD_and_QD_should_return_0(self):
        result = self.deng.check(['JD', 'QC'])
        self.assertEqual(result, 0)

    def test_players_get_2d_and_5c_cards_should_return_7(self):
        result = self.deng.check(['2D', '5C'])
        self.assertEqual(result, 7)

    def test_players_get_3d_and_5c_cards_should_return_8(self):
        result = self.deng.check(['3D', '5C'])
        self.assertEqual(result, 8)

    def test_player_a_got_2_player_b_got_9_should_return_b_won(self):
        player_a_score = self.deng.check['2D', 'KD']
        player_b_score = self.deng.check['5D', '4d']
        self.assertEqual(result, 'b won')

class Deng:
    def check(self, cards):
        result = 0
        faces = ['K', 'Q', 'J']
        for card in cards:
            if card[0] in faces:
                result += 0
            else:
                result += int(card[0])
        return result


if __name__ == '__main__':
    unittest.main()

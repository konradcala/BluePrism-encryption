import logging
from unittest import TestCase

from security.blue_prism_aes import BluePrismAes


class TestBluePrismAes(TestCase):
    logging.basicConfig(level=logging.DEBUG)
    aes = BluePrismAes('LOm/OeAd4NpwKjA5CTgZGaRLqzXd0ii4a/IxYzYnGnY=')

    def test_decrypt(self):
        # given
        with open('test/resources/security/encrypted_queue_item_data.txt') as res_file:
            encrypted_item = res_file.read()
        with open('test/resources/security/decrypted_queue_item_data.xml') as res_file:
            expected_decrypted_data_item = res_file.read()

        # when
        result = self.aes.decrypt(encrypted_item)

        # then
        self.assertEqual(expected_decrypted_data_item, result)

    def test_encrypt(self):
        with open('test/resources/security/decrypted_queue_item_data.xml') as res_file:
            expected_decrypted_data_item = res_file.read()

        # when
        encrypted_result = self.aes.encrypt(expected_decrypted_data_item)
        decrypted_result = self.aes.decrypt(encrypted_result)

        # then
        self.assertEqual(decrypted_result, expected_decrypted_data_item)
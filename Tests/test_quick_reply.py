import unittest

from decouple import config
from messenger_bot.template.template_quick_reply import QuickReply
from messenger_bot.utility.tag import Tags

from Tests.send_message import Facebook


class TestQuickReply(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.facebook = Facebook()
        cls.test_user = config("test_facebook_user", None)

    @classmethod
    def tearDownClass(cls):
        del cls.facebook

    def test_case_one_two(self):
        """
        This the only test functions contains 5 phases. 
        """
        q_reply = QuickReply(self.test_user)

        # ---------------------------------------
        # Test Phase 1 & 2
        # ---------------------------------------
        test_1_payload = q_reply.quick_reply_create("text", "Hello_World")
        self.assertEqual(test_1_payload, {},
                         "Its suppose to be an empty dictionary here!")
        test_2_payload = q_reply.quick_reply_create(
            "text", "Hello_World", "123456", "")

        test_1_quick_reply_payload = q_reply.quick_reply(
            "test_case_one_two", [test_1_payload])
        test_2_quick_reply_payload = q_reply.quick_reply(
            "test_case_one_two", [test_2_payload])

        self.assertNotEqual(type(test_1_quick_reply_payload), dict,
                            "Test_1 You shall not Pass")
        self.assertEqual(type(test_2_quick_reply_payload), dict,
                         "Test_2 This is suppose to be a dictionary to be passed!")
        status_code = self.facebook.send_message(test_1_quick_reply_payload)
        self.assertEqual(status_code, 400,
                         "This test case must be 400!")
        status_code = self.facebook.send_message(test_2_quick_reply_payload)
        self.assertEqual(status_code, 200, "This better be 200!")

    def test_case_three(self):
        # ---------------------------------------
        # Test phase 3:
        # ---------------------------------------
        # Run All Text based - 13 in total. All goes normal. Nothings Changed
        q_reply = QuickReply(self.test_user)
        test_3_payload = list()
        for _ in range(0, 13):
            title_text = "test_case_three {}".format(_)
            payload = "123123dfjf"
            image_url = "https://developers.facebook.com/docs/messenger-platform/reference/send-api/quick-replies/"
            test_3_payload.append(q_reply.quick_reply_create(
                "text", title_text=title_text, payload=payload, image_url=image_url))
        test_3_quick_reply_payload = q_reply.quick_reply(
            "Title Text", test_3_payload)
        self.assertEqual(type(test_3_quick_reply_payload), dict, "Oh Crap!")
        status_code = self.facebook.send_message(test_3_quick_reply_payload)
        self.assertEqual(status_code, 200, "All Should go normal here!")

    def test_case_four(self):
        # ---------------------------------------
        # Test Phase 4
        # ---------------------------------------
        # This test case is suppose to break down somewhere down the line.
        # This will be random Totes
        q_reply = QuickReply(self.test_user)
        test_4_payload = list()
        for _ in range(0, 11):
            title_text = "test_case_four {}".format(_)
            payload = "vikings_{}".format(_)
            image_url = config("test_url", None)

            import random
            x = random.randint(2, 10)

            if x % 2:
                content_type = Tags.TAG_CONTENT_TYPE_TEXT
            elif x % 3:
                content_type = Tags.TAG_CONTENT_TYPE_LOCATION
            elif x % 5:
                content_type = Tags.TAG_CONTENT_TYPE_USER_PHONE_NUMBER
            else:
                content_type = Tags.TAG_CONTENT_TYPE_USER_EMAIL

            test_4_payload.append(q_reply.quick_reply_create(
                content_type, title_text, payload, image_url))

        test_4_quick_reply_payload = q_reply.quick_reply(
            "Test 4 Quick Reply Payload", test_4_payload)
        self.assertEqual(type(test_4_quick_reply_payload),
                         dict, "Oh Crap!")
        status_code = self.facebook.send_message(
            test_4_quick_reply_payload)
        self.assertEqual(status_code, 400,
                         "This test case is suppose to breakdown!")

    def test_case_five(self):
        q_reply = QuickReply(self.test_user)
        # ---------------------------------------
        # Test Phase 5
        # ---------------------------------------
        test_5_payload = list()
        for _ in range(0, 14):
            title_text = "test_case_five {}".format(_)
            payload = "vikings_{}".format(_)
            image_url = config("test_url", None)

            print("Image URL is: {}".format(image_url))

            import random
            x = random.randint(2, 10)

            if x % 2:
                content_type = Tags.TAG_CONTENT_TYPE_TEXT
            elif x % 3:
                content_type = Tags.TAG_CONTENT_TYPE_LOCATION
            elif x % 5:
                content_type = Tags.TAG_CONTENT_TYPE_USER_PHONE_NUMBER
            else:
                content_type = Tags.TAG_CONTENT_TYPE_USER_EMAIL

            test_5_payload.append(q_reply.quick_reply_create(
                content_type, title_text, payload, image_url))

        test_5_quick_reply_payload = q_reply.quick_reply(
            "Test 5 Quick Reply Payload", test_5_payload)
        self.assertEqual(type(test_5_quick_reply_payload),
                         type(None), "Oh Crap!")
        status_code = self.facebook.send_message(test_5_quick_reply_payload)
        self.assertEqual(status_code, 400, "This better be 400!")

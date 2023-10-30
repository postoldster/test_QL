from faker import Faker

class FakeData:

    fake = Faker()

    def generate_fake_data(self, entities_number):
        address_book = []
        for i in range(entities_number):
            address_entry = {
                "full_name": self.fake.name(),
                "user_email": self.fake.email(),
                "current_address": self.fake.address().replace('\n', ' '),
                "permanent_address": self.fake.address().replace('\n', ' '),
            }
            address_book.append(address_entry)
        return address_book


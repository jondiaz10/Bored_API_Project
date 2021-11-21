import requests as request


class ActivityGenerator:

    def __init__(self):
        pass

    def decide_activity(self):

        deciding = True
        act_call = ActivityCaller()
        valid_types = ['education', 'recreational', 'social', 'diy', 'charity', 'cooking', 'relaxation', 'music',
                       'busywork']

        while deciding:

            choice = input("Are you Bored? Yes or No").lower()

            while choice not in ['yes', 'no']:
                choice = input('Please enter a valid option. Are you Bored? Yes or No').lower()

            if choice == 'yes':
                type_pref = input('Do you Have a specific Activity Preference? Yes or No').lower()
                while type_pref not in ['yes', 'no']:
                    type_pref = input(
                        'Please enter a valid option. Do you Have a specific Activity Preference? Yes or No').lower()
                if type_pref == 'yes':
                    type_choice = input('Please choose from the following: education, recreational, social, diy, '
                                        'charity, cooking, relaxation, music, busywork').lower()
                    while type_choice not in valid_types:
                        type_choice = input('Please choose from the following: education, recreational, social, diy, '
                                            'charity, cooking, relaxation, music, busywork').lower()
                    if type_choice in valid_types:
                        act_call.get_activity(act_type=type_choice)
                        act_call.print_activity()
                        not_satisfied = True
                        while not_satisfied:
                            satisfied_answer = input('Are you satisfied with this activity? Yes or No').lower()
                            while satisfied_answer not in ['yes', 'no']:
                                satisfied_answer = input(
                                    'Please enter a valid option. Are you satisfied with this answer? Yes or No').lower()
                            if satisfied_answer == 'yes':
                                print()
                                print('Thank you for using the activity generator')
                                not_satisfied = False
                                deciding = False
                            else:
                                change_choice = input('Would you like to change your activity? Yes or No').lower()
                                while change_choice not in ['yes', 'no']:
                                    change_choice = input('Please enter a valid option. Would you like to change your '
                                                          'activity? Yes or No').lower()
                                if change_choice == 'yes':
                                    type_choice = input(
                                        'Please choose from the following: education, recreational, social, diy, '
                                        'charity, cooking, relaxation, music, busywork').lower()
                                    while type_choice not in valid_types:
                                        type_choice = input(
                                            'Please choose from the following: education, recreational, social, diy, '
                                            'charity, cooking, relaxation, music, busywork').lower()
                                    act_call.get_activity(act_type=type_choice)
                                    act_call.print_activity()
                                else:
                                    act_call.get_activity(act_type=type_choice)
                                    act_call.print_activity()

                else:
                    act_call.get_activity()
                    act_call.print_activity()
                    not_satisfied = True
                    while not_satisfied:
                        satisfied_answer = input('Are you satisfied with this activity? Yes or No').lower()
                        while satisfied_answer not in ['yes', 'no']:
                            satisfied_answer = input(
                                'Please enter a valid option. Are you satisfied with this answer? Yes or No').lower()
                        if satisfied_answer == 'yes':
                            print()
                            print('Thank you for using the activity generator')
                            not_satisfied = False
                            deciding = False
                        else:
                            act_call.get_activity()
                            act_call.print_activity()


            else:
                print('Have a Fun Day!')
                deciding = False


class ActivityCaller:

    def __init__(self):
        self.activity = ''
        self.type = ''
        self.participants = 0
        self.price = 0
        self.link = ''
        self.activity_key = ''
        self.accessibility = 0

    def get_activity(self, act_type=''):
        self.url = Url_Generator(act_type).generate().url
        response = request.get(self.url).json()
        self.activity = response['activity']
        self.type = response['type']
        self.participants = response['participants']
        self.price = response['price']
        self.link = response['link']
        self.accessibility = response['accessibility']
        self.activity_key = response['key']
        return self

    def print_activity(self):
        print('-----------------------')
        print(f' Your Randomly Chosen Activity: {self.activity}')
        print(f' Activity Type: {self.type}')
        print(f' Participants: {self.participants}')
        print(f' Activity Price: {self.price}')
        print(f' Activity Link: {self.link}')
        print(f' Activity Accessibility: {self.accessibility}')
        print(f' Activity ID: {self.activity_key}')


class Url_Generator:

    def __init__(self, act_type):
        self.base_url = 'http://www.boredapi.com/api/activity'
        self.type = act_type

    def generate(self):
        if self.type == '':
            self.url = self.base_url
        else:
            self.url = f'{self.base_url}?type={self.type}'
        return self


activity_caller = ActivityGenerator()
activity_caller.decide_activity()

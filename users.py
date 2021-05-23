import numpy as np

class User:
    """ Optimizes their experience. Gain.
    """
    def __init__(self, unique_id, model):
        self.unique_id = unique_id
        # self.friends = list()
        # self.cur_entertainment = 0
        self.model = model
        self.utility_func = np.random.choice(self.model.param['possible_preferences_functions'])
        self.utility_lower_bound = np.random.uniform(-1, 1)
        self.platform_choices = list()
        self.page_choices = list()
        self.stay_durations  = list()

    def go_to_pages(self):
        if stay_durations[-1] == 0 or len(stay_durations) == 0:
            chosen_platform_pages = self.platform_choices[-1].pages
            pages_w = [page.w for page in chosen_platform_pages]
            cur_page_choices = []
            utility_from_pages = list(map(pref_func, pages_w))
            for list_index, utility in enum(utility_from_page):
                if utility >= self.utility_lower_bound:
                    chosen_platform_pages[list_index].visits += 1
                    cur_page_choices.append(chosen_platform_pages[list_index])
            self.page_choices.append(cur_page_choices)

    def decision_to_stay(self):
        if stay_durations[-1] == 0 or len(stay_durations) == 0:
            if len(page_choices[-1]) > 0:
                self.stay_decision = np.random.choice([False, True])
                if stay_decision == True:
                    self.platform_choices[-1].active_users_count += 1
                    chosen_platform_pages = page_choices[-1]
                    total_utility = np.sum(np.array([page.w for page in chosen_platform_pages]))
                    duration = int(round(total_utility))
                    stay_durations.append(duration)
                    for page in chosen_platform_pages:
                        page.time_spent += duration

            else:
                self.stay_durations[-1] = 0
        else:
            self.stay_durations[-1] -= 1
            if self.stay_durations[-1] == 0:
                self.platform_choices[-1].active_users_count -= 1

    def add_friend(self, friend):
        self.append(friend)

    def choose_platform(self):
        if stay_durations[-1] == 0 or len(stay_durations) == 0:
            current_platform_choice = np.random.choice(model.platforms)
            self.platform_choices.append(current_platform_choice)

            current_platform_choice.visits += 1

    def step(self):
        self.choose_platform()
        self.go_to_pages()
        self.decision_to_stay()

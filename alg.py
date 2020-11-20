import statistics
# for item in main.survey_answers:
#     if item.work_interference == 'Often':
#         print(item)
class Alg:
    def calculate_median_age_often(self, all_answers, all_ages, answered_often, ages_often):
        for item in all_answers:
            all_ages.append(item.age)
            # print(sum(survey_answers_ages)/len(survey_answers_ages))
            if item.work_interference == 'Often':
                answered_often.append(item)
        for item1 in answered_often:
            ages_often.append(item1.age)
        # print(ages_ans_often)
        num_ans_often = statistics.median(ages_often)
        return num_ans_often

    def calculate_median_age_sometimes(self, all_answers, all_ages, answered_sometimes, ages_sometimes):
        for item in all_answers:
            all_ages.append(item.age)
            # print(sum(survey_answers_ages)/len(survey_answers_ages))
            if item.work_interference == 'Sometimes':
                answered_sometimes.append(item)
        for item1 in answered_sometimes:
            ages_sometimes.append(item1.age)
        # print(ages_ans_often)
        num_ans_often = statistics.median(ages_sometimes)
        return num_ans_often

    def calculate_median_age_fem_often(self, all_answers, all_answers_fem,
                                       answered_often_fem, ages_often_fem):
        for item in all_answers:
            all_answers_fem.append(item.age)
            # print(sum(survey_answers_ages)/len(survey_answers_ages))
            if item.work_interference == 'Often' and (
                    item.gender == 'F' or item.gender == 'Female' or item.gender == 'f'
                    or item.gender == 'female'):
                answered_often_fem.append(item)
        for item1 in answered_often_fem:
            ages_often_fem.append(item1.age)
        # print(ages_ans_often)
        num_ans_often_fem = statistics.median(ages_often_fem)
        return num_ans_often_fem

    def calculate_median_age_fem_sometimes(self, all_answers, all_answers_fem, answered_sometimes_fem, ages_sometimes_fem):
        for item in all_answers:
            all_answers_fem.append(item.age)
            # print(sum(survey_answers_ages)/len(survey_answers_ages))
            if item.work_interference == 'Sometimes' and (
                    item.gender == 'F' or item.gender == 'Female' or item.gender == 'f' or item.gender == 'female'):
                answered_sometimes_fem.append(item)
        for item1 in answered_sometimes_fem:
            ages_sometimes_fem.append(item1.age)
        # print(ages_ans_often)
        num_ans_often_fem = statistics.median(ages_sometimes_fem)
        return num_ans_often_fem

    def calculate_median_age_male_often(self, all_answers, all_answers_male, answered_often_male, ages_often_male):
        for item in all_answers:
            all_answers_male.append(item.age)
            # print(sum(survey_answers_ages)/len(survey_answers_ages))
            if item.work_interference == 'Often' and (
                    item.gender == 'M' or item.gender == 'Male' or item.gender == 'm' or item.gender == 'male'):
                answered_often_male.append(item)
        for item1 in answered_often_male:
            ages_often_male.append(item1.age)
        # print(ages_ans_often)
        num_ans_often_male = statistics.median(ages_often_male)
        return num_ans_often_male

    def calculate_median_age_male_sometimes(self, all_answers, all_answers_male, answered_sometimes_male, ages_sometimes_male):
        for item in all_answers:
            all_answers_male.append(item.age)
            # print(sum(survey_answers_ages)/len(survey_answers_ages))
            if item.work_interference == 'Sometimes' and (
                    item.gender == 'M' or item.gender == 'Male' or item.gender == 'm' or item.gender == 'male'):
                answered_sometimes_male.append(item)
        for item1 in answered_sometimes_male:
            ages_sometimes_male.append(item1.age)
        # print(ages_ans_often)
        num_ans_often_male = statistics.median(ages_sometimes_male)
        return num_ans_often_male

    def calculate_median_age_other_often(self, all_answers, all_answers_other, answered_often_other, ages_often_other):
        for item in all_answers:
            all_answers_other.append(item.age)
            # print(sum(survey_answers_ages)/len(survey_answers_ages))
            if item.work_interference == 'Often' and (item.gender != 'm' and item.gender != 'M' and item.gender != 'male' and item.gender != 'Male' and item.gender != 'f' and \
                                item.gender !='F' and item.gender !='Female' and item.gender !='female' and item.gender !='Cis Female'\
                    and item.gender !='Cis male'):
                answered_often_other.append(item)
        for item1 in answered_often_other:
            ages_often_other.append(item1.age)
        # print(ages_ans_often)
        num_ans_often_other = statistics.median(ages_often_other)
        return num_ans_often_other

    def calculate_median_age_other_sometimes(self, all_answers, all_answers_other, answered_sometimes_other, ages_sometimes_other):
        for item in all_answers:
            all_answers_other.append(item.age)
            # print(sum(survey_answers_ages)/len(survey_answers_ages))
            if item.work_interference == 'Sometimes' and (item.gender != 'm' and item.gender != 'M' and item.gender != 'male' and item.gender != 'Male' and item.gender != 'f' and \
                                item.gender !='F' and item.gender !='Female' and item.gender !='female' and item.gender !='Cis Female'\
                    and item.gender !='Cis male'):
                answered_sometimes_other.append(item)
        for item1 in answered_sometimes_other:
            ages_sometimes_other.append(item1.age)
        # print(ages_ans_often)
        num_ans_sometimes_other = statistics.median(ages_sometimes_other)
        return num_ans_sometimes_other






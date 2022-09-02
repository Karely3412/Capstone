class competency_summary:
    def __init__(self, arr):
        self.name = str(arr[0])
        self.email = str(arr[1])
        self.assessments = arr[2]
        self.competencies_num = arr[3]
        self.calculate_average_competency_score()

    def calculate_average_competency_score(self):
        total = 0
        for val in self.assessments:
            total = total + val.get_score()
        self.average_competency_score = total / self.competencies_num

    def get_average_competency_score(self):
        return self.average_competency_score

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_assessments(self):
        return self.assessments

    def get_competencies_num(self):
        return self.competencies_num

class assessment:
    def __init__(self, arr):
        self.assessment_score = int(arr[0])
        self.assessment_name = arr[1]
        self.competency_name = arr[2]

    def get_score(self):
        return self.assessment_score

    def get_assessment_name(self):
        return self.assessment_name

    def get_competency_name(self):
        return self.competency_name

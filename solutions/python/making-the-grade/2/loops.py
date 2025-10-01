"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    for score in range(len(student_scores)):
        student_scores[score] = round(student_scores[score])
    return student_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    fail_count = 0
    for index, score in enumerate(student_scores):
        if score < 41:
            fail_count +=1
    return fail_count

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    high_scorers = []
    for index, score in enumerate(student_scores):
        if score >= threshold:
            high_scorers.append(score)
    return high_scorers
    
def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    grade_increment = (highest - 40) // 4
    grade_thresholds = []
    for increment in range(4):
        grade_thresholds.append(41 + (grade_increment * increment))
    for index, grades in enumerate(grade_thresholds):
        grade_thresholds[index] = round(grades)
    return grade_thresholds

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    student_rank = []
    for index, name in enumerate(student_names, start=1):
        student_rank.append(f"{index}. {name}: {student_scores[index -1]}")
    return student_rank

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    
    for index, list_num in enumerate(student_info):
        if 100 in list_num:
            return student_info[index]
    return []

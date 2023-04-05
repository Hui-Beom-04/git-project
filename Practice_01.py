submit_credit, submit_gpa, archive_credit, archive_gpa = 0, 0, 0, 0


while True:
    print("작업을 선택하세요")
    print("    1. 입력")
    print("    2. 계산")
    choose = int(input())

    if choose == 1:
        print("학점을 입력하세요:")
        credit = int(input())
        print("평점을 입력하세요:")
        grade = input()
        print("입력되었습니다.")

        match grade:
            case 'A+':
                gpa = 4.5
                submit_credit += credit
                submit_gpa += credit * gpa
                archive_credit += credit
                archive_gpa += credit * gpa

            case 'A':
                gpa = 4.0
                submit_credit += credit
                submit_gpa += credit * gpa
                archive_credit += credit
                archive_gpa += credit * gpa

            case 'B+':
                gpa = 3.5
                submit_credit += credit
                submit_gpa += credit * gpa
                archive_credit += credit
                archive_gpa += credit * gpa

            case 'B':
                gpa = 3.0
                submit_credit += credit
                submit_gpa += credit * gpa
                archive_credit += credit
                archive_gpa += credit * gpa

            case 'C+':
                gpa = 2.5
                submit_credit += credit
                submit_gpa += credit * gpa
                archive_credit += credit
                archive_gpa += credit * gpa

            case 'C':
                gpa = 2.0
                submit_credit += credit
                submit_gpa += credit * gpa
                archive_credit += credit
                archive_gpa += credit * gpa

            case 'D+':
                gpa = 1.5
                submit_credit += credit
                submit_gpa += credit * gpa
                archive_credit += credit
                archive_gpa += credit * gpa

            case 'D':
                gpa = 1.0
                submit_credit += credit
                submit_gpa += credit * gpa
                archive_credit += credit
                archive_gpa += credit * gpa

            case 'F':
                gpa = 0
                archive_credit += credit
                archive_gpa += credit * gpa


    else:
        print("제출용: " + str(submit_credit) + "  (GPA: " + str(submit_gpa/submit_credit) + ")")
        print("열람용: " + str(archive_credit) + "  (GPA: " + str(archive_gpa/archive_credit) + ")")
        break


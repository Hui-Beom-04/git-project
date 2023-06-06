# 수강정보 클래스
class CourseRecord:
    # 생성자
    def __init__(self, course_id, course_name, credit, grade):
        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit
        self.grade = grade
    
    # 문자열 특별 메서드
    def __str__(self):
        string = f'[{self.course_name}] {self.credit}학점: {self.grade}'
        return string
    
    @classmethod
    def get_gpa_score(cls, gpa):
        match gpa:
            case 'A+':
                return 4.5
            case 'A':
                return 4
            case 'B+':
                return 3.5
            case 'B':
                return 3
            case 'C+':
                return 2.5
            case 'C':
                return 2
            case 'D+':
                return 1.5
            case 'D':
                return 1
            case 'F':
                return 0

            
# 수강목록 클래스
class CourseHistory:    
    # 생성자
    def __init__(self):
        self.history = []
        self.course_id_map = {'id': 10000}
        self.submit_grade = {}
        self.archive_grade = {}
        
        self.filename = "course_history.csv"
    
    # 점수 변환 함수
    def allocate_course_id(self, course_name):
        if course_name not in self.course_id_map:
            new_id = str(int(self.course_id_map['id']) + 1)
            self.course_id_map['id'] = new_id
            self.course_id_map[course_name] = new_id
            self.course_id_map[new_id] = course_name

            return new_id

        else:
            return self.course_id_map[course_name]
        
    # 입력 함수
    def input_process(self):
        course_name = input('과목명을 입력하세요: ')
        course_id = self.allocate_course_id(course_name)

        credit = input('학점을 입력하세요: ')
        credit = int(credit)
        
        gpa = input('평점을 입력하세요: ')
        gpa_score = CourseRecord.get_gpa_score(gpa)
        
        # 열람용 학점 처리
        if course_id in self.archive_grade:
            # 재수강 처리
            if gpa_score > self.archive_grade[course_id][1]:
                self.archive_grade[course_id] = (credit, gpa_score)
        else:
            self.archive_grade[course_id] = (credit, gpa_score)
            
        # 제출용 학점 처리
        if gpa_score > 0.0:
            if course_id in self.submit_grade:
                # 재수강 처리
                if gpa_score > self.submit_grade[course_id][1]:
                    self.submit_grade[course_id] = (credit, gpa_score)
            else:
                self.submit_grade[course_id] = (credit, gpa_score)

        course_record = CourseRecord(course_id, course_name, credit, gpa)
        self.history.append(course_record)
        

    # 출력 함수
    def print_process(self):
        for course_record in self.history:
            print(course_record)
    
    # 조회 함수
    def query_process(self):
        course_name = input('과목명을 입력하세요: ')
        
        for course_record in self.history:
            if course_name == course_record.course_name:
                print(course_record)
        else:
            print('해당하는 과목이 없습니다.')
        
    # 계산 함수
    def calculate_process(self):
        submit_gpa, archive_gpa = 0.0, 0.0
        submit_credit, archive_credit = 0, 0
        
        for course_id in self.submit_grade:
            submit_gpa += self.submit_grade[course_id][0] * self.submit_grade[course_id][1]
            submit_credit += self.submit_grade[course_id][0]
            
        for course_id in self.archive_grade:
            archive_gpa += self.archive_grade[course_id][0] * self.archive_grade[course_id][1]
            archive_credit += self.archive_grade[course_id][0]
            
        submit_gpa /= submit_credit
        archive_gpa /= archive_credit
        
        # print('제출용: ' + str(submit_credit) + '학점' + '(GPA: ' + str(submit_gpa) + ')')
        # print('열람용: ' + str(archive_credit) + '학점' + '(GPA: ' + str(archive_gpa) + ')')
        print(f'제출용: {submit_credit} 학점(GPA: {submit_gpa})')
        print(f'열람용: {archive_credit} 학점(GPA: {archive_gpa})')
        
    # 파일 저장 함수
    def save_process(self):
        with open(self.filename, 'w') as file:
            # history 내의 모든 과목정보에 대해 반복
            for course in self.history:
                # 파일 쓰기
                file.write(f'{course.course_id},{course.course_name},{course.credit},{course.grade}\n')

            print(f'파일로 저장되었습니다.')
    
    # 파일 불러오기 함수
    def load_process(self):
        with open(self.filename, 'r') as file:
            # 파일 첫 줄 읽기
            file_string = file.readline()
            
            # 읽어온 줄이 존재한다면 반복문 실행
            while file_string != '':
                # 새줄문자로 끝날 경우 새줄문자 제거
                if file_string[-1] == '\n':
                    file_string = file_string[:-1]
                
                # 콤마(',')를 기준으로 문자 나누기
                tokens = file_string.split(',')
                course_id = int(tokens[0])
                course_name = tokens[1]
                credit = int(tokens[2])
                grade = tokens[3]
                
                # 새 과목정보 만들기
                course_record = CourseRecord(course_id, course_name, credit, grade)
                
                # 새 과목정보 저장하기
                self.history.append(course_record)
                
                # 과목코드 수정하기 (파일에서 읽어온 과목코드가 인스턴스가 보유한 가장 높은 과목코드보다 크다면 정보 갱신)
                ## 이 프로그램에서는 과목이 추가될 때마다 과목코드가 1씩 증가하면서 할당됩니다.
                ## 그러므로 self.history의 가장 마지막 과목이 가장 높은 과목코드를 가집니다.
                ## 이밖에도 다양한 과목정보 관리방법이 존재하며 그 중에는 이보다 효율적인 방법도 있습니다.
                ## 하지만 파이썬을 처음 공부하는 입장에서는 이 정도의 로직을 생각할 수 있는 것만으로도 충분합니다.
                if self.course_id_map['id'] < course_id:
                    self.course_id_map['id'] = course_id
                    
                # 과목코드 매핑 추가하기
                self.course_id_map[course_name] = course_id
                self.course_id_map[course_id] = course_name
                
                # 파일에서 다음 한 줄 읽기
                file_string = file.readline()
                
            print(f'파일을 불러왔습니다.')

def read_number(prompt, minimum, maximum):
    while True:
        text = input(prompt).strip()
        if not text:
            print("번호를 입력해주세요.")
            continue

        try:
            number = int(text)
        except ValueError:
            print("숫자로 입력해주세요.")
            continue

        if minimum <= number <= maximum:
            return number

        print(f"{minimum}~{maximum} 사이의 번호를 입력해주세요.")


class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        print(self.question)
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer


def create_default_quizzes():
    return [
        Quiz(
            "Python에서 값을 이름에 연결해 나중에 사용할 때 쓰는 것은?",
            ["주석", "변수", "폴더", "커밋"],
            2,
        ),
        Quiz(
            "Python에서 정수를 나타내는 자료형은?",
            ["str", "bool", "int", "list"],
            3,
        ),
        Quiz(
            "Python에서 조건에 따라 실행할 코드를 나눌 때 사용하는 것은?",
            ["if / elif / else", "print", "input", "import"],
            1,
        ),
        Quiz(
            "Python에서 함수가 결과값을 호출한 곳으로 돌려줄 때 사용하는 것은?",
            ["continue", "break", "pass", "return"],
            4,
        ),
        Quiz(
            "Git에서 준비된 변경 사항을 로컬 저장소의 이력으로 기록하는 명령은?",
            ["git push", "git commit", "git clone", "git pull"],
            2,
        ),
    ]


class QuizGame:
    def __init__(self):
        self.quizzes = create_default_quizzes()

    def show_menu(self):
        print("\n========================================")
        print("       Python · Git 복습 퀴즈")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def run(self):
        while True:
            self.show_menu()
            choice = read_number("선택: ", 1, 5)

            if choice == 1:
                print("퀴즈 풀기 기능을 준비 중입니다.")
            elif choice == 2:
                print("퀴즈 추가 기능을 준비 중입니다.")
            elif choice == 3:
                print("퀴즈 목록 기능을 준비 중입니다.")
            elif choice == 4:
                print("점수 확인 기능을 준비 중입니다.")
            elif choice == 5:
                print("퀴즈 게임을 종료합니다.")
                break


if __name__ == "__main__":
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 퀴즈 게임을 종료합니다.")

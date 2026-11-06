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


def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("내용을 입력해주세요.")


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

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        total = len(self.quizzes)
        correct_count = 0
        print(f"\n퀴즈를 시작합니다! (총 {total}문제)")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n----------------------------------------\n[문제 {number}]")
            quiz.display()
            user_answer = read_number("정답 입력 (1~4): ", 1, 4)

            if quiz.check_answer(user_answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        score = round(correct_count / total * 100)
        print(f"\n결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")

    def add_quiz(self):
        print("\n새로운 퀴즈를 추가합니다.")
        question = read_text("문제를 입력하세요: ")
        choices = []
        for number in range(1, 5):
            choice = read_text(f"선택지 {number}: ")
            choices.append(choice)
        answer = read_number("정답 번호 (1~4): ", 1, 4)

        quiz = Quiz(question, choices, answer)
        self.quizzes.append(quiz)
        print(f"퀴즈가 추가되었습니다! (총 {len(self.quizzes)}개)")

    def list_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("----------------------------------------")

    def run(self):
        while True:
            self.show_menu()
            choice = read_number("선택: ", 1, 5)

            if choice == 1:
                self.play()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
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

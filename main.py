class QuizGame:
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
            choice = input("선택: ").strip()

            if choice == "1":
                print("퀴즈 풀기 기능을 준비 중입니다.")
            elif choice == "2":
                print("퀴즈 추가 기능을 준비 중입니다.")
            elif choice == "3":
                print("퀴즈 목록 기능을 준비 중입니다.")
            elif choice == "4":
                print("점수 확인 기능을 준비 중입니다.")
            elif choice == "5":
                print("퀴즈 게임을 종료합니다.")
                break
            else:
                print("1~5 사이의 번호를 입력해주세요.")


if __name__ == "__main__":
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 퀴즈 게임을 종료합니다.")

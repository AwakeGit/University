import subprocess
import datetime

def run_command(command):
    """Функция для выполнения команды в терминале."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        print(f"Ошибка при выполнении команды: {command}\n{result.stderr}")
        return None

def clean_repo():
    """Функция для полной очистки репозитория."""
    print("Очищаем изменения в отслеживаемых файлах...")
    run_command('git reset --hard')

    print("Удаляем неотслеживаемые файлы...")
    run_command('git clean -fd')

    print("Репозиторий полностью очищен от всех изменений.")

def merge_dev_to_prd():
    """Функция для автоматического переноса ревизии из dev в prd с установкой тэга."""
    target_branch = 'prd'

    print("Переключаемся на ветку dev и подтягиваем изменения...")
    run_command('git checkout dev')
    run_command('git pull origin dev')

    print(f"Переключаемся на ветку {target_branch} и подтягиваем изменения...")
    run_command(f'git checkout {target_branch}')
    run_command(f'git pull origin {target_branch}')

    print("Выполняем слияние dev в prd...")
    merge_result = run_command('git merge dev')

    if merge_result:
        print("Слияние прошло успешно.")
        tag_name = f"release-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
        print(f"Добавляем тег {tag_name}...")
        run_command(f'git tag -a {tag_name} -m "Auto-release from dev to prd on {datetime.datetime.now()}"')

        print("Отправляем изменения и тег в удаленный репозиторий...")
        run_command(f'git push origin {target_branch}')
        run_command(f'git push origin {tag_name}')

        print(f"Изменения из dev успешно перенесены в prd с тегом {tag_name}.")
    else:
        print("Слияние не удалось. Проверьте конфликтные файлы.")

if __name__ == "__main__":
    print("Выберите операцию:")
    print("1. Полная очистка репозитория")
    print("2. Автоматический перенос ревизии из dev в prd с установкой тэга")

    choice = input("Введите 1 или 2: ")

    if choice == "1":
        clean_repo()
    elif choice == "2":
        merge_dev_to_prd()
    else:
        print("Неверный выбор.")

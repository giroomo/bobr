import requests
import datetime

# Константы
HN_API_TOP = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_API_ITEM = "https://hacker-news.firebaseio.com/v0/item/{}.json"
DIGEST_FILE = "daily_digest.md"


def get_top_stories(limit=5):
    """Получает топ-5 ID статей."""
    try:
        response = requests.get(HN_API_TOP)
        response.raise_for_status()
        return response.json()[:limit]
    except Exception as e:
        print(f"Ошибка API: {e}")
        return []


def get_story_details(story_id):
    """Получает детали одной статьи."""
    try:
        url = HN_API_ITEM.format(story_id)
        return requests.get(url).json()
    except Exception:
        return None


def create_markdown_content(stories):
    """Генерирует текст для Markdown."""
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    content = f"# 📢 Ежедневный дайджест новостей ({date_str})\n\n"

    for story in stories:
        if not story:
            continue
        title = story.get('title', 'Без заголовка')
        link = story.get('url', '#')
        score = story.get('score', 0)
        content += f"### [{title}]({link})\n"
        content += f"**Рейтинг:** {score} 🔥\n\n"
        content += "---\n"

    return content


def main():
    ids = get_top_stories()
    full_stories = [get_story_details(sid) for sid in ids]
    markdown_text = create_markdown_content(full_stories)

    # Сохраняем/Перезаписываем файл
    with open(DIGEST_FILE, "w", encoding="utf-8") as f:
        f.write(markdown_text)
    print(f"Дайджест обновлен: {DIGEST_FILE}")


if __name__ == "__main__":
    main()
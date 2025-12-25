from src.main import create_markdown_content


def test_create_markdown_content():
    # Мокаем данные (тестовые данные)
    mock_stories = [
        {"title": "Python 3.12 Released", "url": "http://python.org", "score": 500},
        {"title": "Why I love Linux", "url": "http://linux.org", "score": 100}
    ]

    result = create_markdown_content(mock_stories)

    # Проверяем, что в тексте есть ключевые слова
    assert "# 📢 Ежедневный дайджест" in result
    assert "Python 3.12 Released" in result
    # Исправили проверку ниже (добавили звездочки):
    assert "**Рейтинг:** 500" in result

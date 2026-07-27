"""Just a placeholder to do relative imports"""

# ©️ Dan Gazizullin, 2021-2023
# This file is a part of Hikka Userbot
# 🌐 https://github.com/hikariatama/Hikka
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html

# ©️ Codrago, 2024-2030
# This file is a part of Heroku Userbot
# 🌐 https://github.com/coddrago/Heroku
# You can redistribute it and/or modify it under the terms of the GNU AGPLv3
# 🔑 https://www.gnu.org/licenses/agpl-3.0.html

# Polyfill emoji module for backwards compatibility with legacy userbot modules
try:
    import emoji

    if not hasattr(emoji, "get_emoji_unicode_dict"):
        def _get_emoji_unicode_dict(lang="en"):
            data = getattr(emoji, "EMOJI_DATA", {})
            return {k: v.get(lang, k) if isinstance(v, dict) else k for k, v in data.items()}
        emoji.get_emoji_unicode_dict = _get_emoji_unicode_dict

    if not hasattr(emoji, "UNICODE_EMOJI"):
        emoji.UNICODE_EMOJI = {"en": getattr(emoji, "EMOJI_DATA", {})}
except Exception:
    pass

__author__ = "Dan Gazizullin"
__ForkAuthor__ = "Codrago"
__contact__ = "me@hikariatama.ru"
__copyright__ = "Copyright 2022, Dan Gazizullin"
__credits__ = ["LonamiWebs", "penn5"]
__license__ = "AGPLv3"
__maintainer__ = "developer"
__status__ = "Production"

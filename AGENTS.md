# AGENTS.md — Heroku Userbot

> This file provides AI coding agents with a comprehensive understanding of the
> Heroku Userbot project: its architecture, conventions, module system, and
> development patterns.

---

## Project Overview

**Heroku** is an advanced Telegram userbot framework written in Python 3.10+.
It is a fork/evolution of [Hikka](https://gitlab.com/hikariatama), built on top
of [Telethon](https://github.com/LonamiWebs/Telethon) (`heroku-tl-new`) for
Telegram MTProto API communication and [Aiogram](https://docs.aiogram.dev/) for
Bot API inline features.

| Attribute       | Value                                   |
| --------------- | --------------------------------------- |
| Version         | 2.0.0                                   |
| Python          | ≥ 3.10                                  |
| License         | AGPL-3.0                                |
| Entry Point     | `python -m heroku`                      |
| Docs (User)     | https://heroku-ub.xyz/                  |
| Docs (Dev)      | https://dev.heroku-ub.xyz/              |
| Repository      | https://github.com/coddrago/Heroku      |

### Key Capabilities

- **Dynamic module loading** — install/unload modules at runtime from URLs or
  local files
- **Multi-language localization** — 5 real languages + 4 meme language packs
- **Inline bot UI** — forms, galleries, lists, and interactive keyboards via
  Telegram Bot API
- **Web authentication UI** — browser-based QR / code login via aiohttp server
- **Security system** — permission bitmaps, access groups, API flood protection
- **Docker deployment** — first-class Docker & docker-compose support
- **Backward compatibility** — runs FTG, GeekTG, and Hikka modules

---

## Repository Structure

```
Heroku/
├── heroku/                     # Main Python package (core framework)
│   ├── __init__.py             # Package marker with metadata
│   ├── __main__.py             # Entry point: pre-flight checks → main.heroku.main()
│   ├── main.py                 # Core execution engine (client, DB, dispatcher, loop)
│   ├── version.py              # Version (2.0.0) and Git branch detection
│   │
│   ├── loader.py               # Module management (load/unload/hot-reload)
│   ├── dispatcher.py           # Event routing to module handlers
│   ├── database.py             # In-memory dict DB with optional Redis sync
│   ├── security.py             # Permission bitmaps & access-control decorators
│   ├── types.py                # Core types: Module, Command, Safe*Proxy, etc.
│   ├── tl_cache.py             # CustomTelegramClient with entity caching
│   ├── validators.py           # Module config validation (Validator, ValidationError)
│   ├── log.py                  # Logging infrastructure & error formatting
│   ├── translations.py         # i18n: Translator, Strings, language management
│   ├── configurator.py         # CLI wizard for API ID/Hash setup
│   ├── qr.py                   # QR code generation (Reed-Solomon encoding)
│   ├── pointers.py             # PointerList/PointerDict → persistent storage
│   ├── _internal.py            # fw_protect, restart, die, get_startup_callback
│   ├── _local_storage.py       # LocalStorage: disk cache for modules
│   ├── _reference_finder.py    # Live object reference replacement via gc
│   ├── _types.py               # Auxiliary type definitions
│   │
│   ├── inline/                 # Telegram Bot API inline capabilities
│   │   ├── core.py             # InlineManager — aggregator of all inline units
│   │   ├── form.py             # Interactive inline forms (Form)
│   │   ├── gallery.py          # Paginated media galleries (Gallery)
│   │   ├── events.py           # Inline/callback query event routing (Events)
│   │   ├── types.py            # InlineCall, InlineMessage, InlineQuery, etc.
│   │   ├── utils.py            # Button styling & markup generation (Utils)
│   │   ├── list.py             # Inline list display
│   │   ├── query_gallery.py    # Inline query gallery handler
│   │   ├── token_obtainment.py # Bot token creation/management
│   │   └── bot_pm.py           # Bot PM handling
│   │
│   ├── web/                    # Web authentication UI (aiohttp)
│   │   ├── core.py             # Web server lifecycle & Jinja2 setup
│   │   ├── root.py             # Auth routes (/send_tg_code, /init_qr_login, …)
│   │   ├── proxypass.py        # SSH tunnel for public URL (ProxyPasser)
│   │   └── ssh_tunnel.py       # Background SSH via serveo.net/localhost.run
│   │
│   ├── secure/                 # TL-level security patches
│   │   ├── __init__.py
│   │   ├── customtl.py         # MTProtoState & ConnectionTcpFull overrides
│   │   └── patcher.py          # Runtime client patching for local proxy
│   │
│   ├── compat/                 # Backward compatibility
│   │   └── geek.py             # GeekTG → Heroku syntax transformer
│   │
│   ├── utils/                  # Utility functions
│   │   ├── __init__.py         # Re-exports all util submodules
│   │   ├── entity.py           # Telegram entity helpers (chats, users, forums)
│   │   ├── messages.py         # Message manipulation (topics, HTML, media)
│   │   ├── platform.py         # Environment detection (Docker, WSL, RPi, …)
│   │   ├── args.py             # Arg parsing, HTML sanitization, reflection
│   │   ├── git.py              # Git operations
│   │   ├── heroku.py           # Heroku platform utilities
│   │   ├── network.py          # Network helpers
│   │   ├── placeholders.py     # Placeholder utilities
│   │   └── other.py            # Miscellaneous utilities
│   │
│   ├── langpacks/              # Localization YAML files
│   │   ├── en.yml              # English
│   │   ├── ru.yml              # Russian
│   │   ├── ua.yml              # Ukrainian
│   │   ├── de.yml              # German
│   │   ├── jp.yml              # Japanese
│   │   ├── leet.yml            # 1337 speak (meme)
│   │   ├── neofit.yml          # Neofit (meme)
│   │   ├── tiktok.yml          # TikTok (meme)
│   │   └── uwu.yml             # UwU (meme)
│   │
│   └── modules/                # Built-in userbot modules (20 modules)
│       ├── api_protection.py   # Rate-limit raw API requests
│       ├── eval.py             # Execute code from Telegram messages
│       ├── help.py             # Help menus & module listings
│       ├── heroku_backup.py    # Database & module backup management
│       ├── heroku_config.py    # Interactive inline config UI
│       ├── heroku_info.py      # System stats & bot status display
│       ├── heroku_plugin_security.py  # External plugin security overrides
│       ├── heroku_security.py  # Command permissions & access groups
│       ├── heroku_settings.py  # Cache clearing, core reloading, settings
│       ├── heroku_web.py       # Web UI authentication & dashboard
│       ├── inline_stuff.py     # Inline query event watchers
│       ├── loader.py           # Dynamic module load/unload/download
│       ├── presets.py          # Curated module preset collections
│       ├── quickstart.py       # Initial setup notifications
│       ├── settings.py         # Core config (prefixes, emoji aliases)
│       ├── terminal.py         # Shell commands from Telegram
│       ├── test.py             # Debug & testing utilities
│       ├── translate.py        # Text translation (Google, MyMemory)
│       ├── translations.py     # Localization management
│       └── updater.py          # Git-based software updates
│
├── assets/                     # Static assets
│   ├── banner.txt              # ASCII art banner
│   ├── font.ttf                # Custom font
│   ├── heroku.png              # Project logo
│   ├── 2fa.txt                 # 2FA prompt text art
│   ├── download.txt            # Download progress text art
│   └── success.txt             # Success message text art
│
├── web-resources/              # Web UI templates & static files
│   ├── base.jinja2             # Base Jinja2 template
│   ├── root.jinja2             # Main login page template
│   └── static/                 # CSS, JS, images for Web UI
│
├── .github/                    # GitHub CI/CD
│   ├── workflows/              # GitHub Actions workflows
│   └── ISSUE_TEMPLATE/         # Issue templates
│
├── Dockerfile                  # Python 3.10-slim + Node.js container
├── docker-compose.yml          # Docker Compose service definition
├── requirements.txt            # Python dependencies
├── optional_requirements.txt   # Optional dependencies
├── install.sh                  # One-line installation script
├── docker.sh                   # Docker build/run helper
├── banner.sh                   # Banner display script
├── README.md                   # English documentation
├── README_RU.md                # Russian documentation
├── CHANGELOG.md                # Version changelog
├── CODE_OF_CONDUCT.md          # Community guidelines
├── LICENSE                     # AGPL-3.0 license
├── .gitignore                  # Git ignore rules
├── .dockerignore               # Docker ignore rules
├── .flake8                     # Flake8 linter config
└── .deepsource.toml            # DeepSource static analysis config
```

---

## Architecture

### Boot Sequence

```
python -m heroku
    └─→ __main__.py
        ├── Check Python ≥ 3.10
        ├── Check root user (warn/override)
        ├── Install/upgrade deps from requirements.txt
        ├── Initialize logging (log.py)
        └── Call main.heroku.main()
              ├── Load config (configurator.py if first run)
              ├── Create CustomTelegramClient (tl_cache.py)
              ├── Connect to Telegram (MTProto)
              ├── Initialize Database (database.py)
              ├── Initialize Translator (translations.py)
              ├── Create InlineManager (inline/core.py)
              ├── Create CommandDispatcher (dispatcher.py)
              ├── Load Modules (loader.py → modules/*.py)
              ├── Start Web UI (web/core.py) [optional]
              └── Run event loop
```

### Core Component Relationships

```
┌─────────────────────────────────────────────────────┐
│                    main.py                          │
│  (orchestrator: creates and connects all components)│
└──────────┬──────────┬──────────┬───────────┬────────┘
           │          │          │           │
     ┌─────▼─────┐ ┌─▼────┐ ┌──▼─────┐ ┌───▼───────┐
     │  tl_cache  │ │  DB  │ │ loader │ │dispatcher │
     │(TG Client) │ │      │ │(Modules│ │ (Events)  │
     └─────┬──────┘ └──┬───┘ └──┬─────┘ └───┬───────┘
           │           │        │            │
           │           │   ┌────▼────┐  ┌────▼────┐
           │           │   │modules/*│  │security │
           │           │   │(plugins)│  │(perms)  │
           │           │   └─────────┘  └─────────┘
           │           │
     ┌─────▼──────┐  ┌▼──────────────┐
     │   inline/  │  │  web/         │
     │(Bot API UI)│  │(Auth Web UI)  │
     └────────────┘  └───────────────┘
```

### Key Classes

| Class                    | File                  | Purpose                                       |
| ------------------------ | --------------------- | --------------------------------------------- |
| `CustomTelegramClient`   | `tl_cache.py`         | Extended Telethon client with entity caching   |
| `Database`               | `database.py`         | In-memory dict DB with Redis sync              |
| `Modules`                | `loader.py`           | Module lifecycle manager                       |
| `CommandDispatcher`      | `dispatcher.py`       | Event → handler routing with security checks   |
| `Module`                 | `types.py`            | Base class for all userbot modules             |
| `InlineManager`          | `inline/core.py`      | Aggregator for all inline Bot API features     |
| `Form`                   | `inline/form.py`      | Interactive inline forms                       |
| `Gallery`                | `inline/gallery.py`   | Paginated inline media galleries               |
| `InlineCall`             | `inline/types.py`     | Callback query wrapper                         |
| `InlineQuery`            | `inline/types.py`     | Inline query wrapper with error helpers        |
| `Web`                    | `web/core.py`         | aiohttp web server for auth UI                 |
| `SecurityGroup`          | `security.py`         | Named tuple for permission groups              |
| `Translator`             | `translations.py`     | i18n manager                                   |
| `Validator`              | `validators.py`       | Module config validation                       |
| `PointerList/PointerDict`| `pointers.py`         | Auto-persisting data structures                |
| `LocalStorage`           | `_local_storage.py`   | Disk cache for downloaded modules              |

### Security Permission Hierarchy

```
OWNER          → Full control (bot owner)
SUDO           → Elevated privileges (deprecated, use groups)
GROUP_OWNER    → Group-specific owner permissions
GROUP_ADMIN_*  → Group admin sub-permissions
  ├── ADD_ADMINS
  ├── CHANGE_INFO
  ├── BAN_USERS
  ├── INVITE_USERS
  ├── PIN_MESSAGES
  └── DELETE_MESSAGES
EVERYONE       → Any user
```

---

## Module Development

### Module Structure

Every module is a Python file in `heroku/modules/` (built-in) or loaded
dynamically. Each module is a class extending `Module` from `heroku.types`:

```python
from .. import loader, utils

class MyModuleMod(loader.Module):
    """Description shown in .help"""

    strings = {"name": "MyModule"}

    async def mycommandcmd(self, message):
        """Command description for .help"""
        await utils.answer(message, "Hello!")
```

### Naming Conventions

- **Module class**: `<Name>Mod` (e.g., `HelpMod`, `LoaderMod`)
- **Command handlers**: `<command>cmd` method → `.command` in Telegram
- **Watcher handlers**: `watcher` method → fires on every message
- **Inline handlers**: `<name>_inline_handler` → responds to inline queries
- **Callback handlers**: `<name>_callback_handler` → responds to button clicks

### Security Decorators

```python
@loader.owner         # Only bot owner
@loader.group_owner   # Group owner
@loader.group_admin   # Group admin
@loader.everyone      # All users
```

### Module Config

Modules can declare configuration using `loader.ModuleConfig`:

```python
config = loader.ModuleConfig(
    loader.ConfigValue(
        "key",
        default_value,
        "Description",
        validator=loader.validators.String(),
    ),
)
```

### Database Access

```python
self.db.get("ModuleName", "key", default)
self.db.set("ModuleName", "key", value)
```

### Inline UI

```python
# Form
await self.inline.form(
    text="Choose option:",
    message=message,
    reply_markup=[
        [{"text": "Option A", "callback": self.callback_a}],
    ],
)

# Gallery
await self.inline.gallery(
    message=message,
    next_handler=self.next_photo,
)
```

---

## Key Dependencies

| Package            | Purpose                                    |
| ------------------ | ------------------------------------------ |
| `heroku-tl-new`    | Telethon fork — Telegram MTProto client    |
| `aiogram`          | Telegram Bot API (inline features)         |
| `aiohttp`          | Async HTTP server (web UI)                 |
| `aiohttp_jinja2`   | Jinja2 template integration for aiohttp    |
| `pydantic`         | Data validation                            |
| `gitpython`        | Git operations for updates                 |
| `ruamel.yaml`      | YAML parsing for language packs            |
| `orjson`           | Fast JSON serialization                    |
| `Pillow`           | Image processing                           |
| `psutil`           | System resource monitoring                 |
| `TgCrypto-pyrofork`| Telegram crypto acceleration               |
| `bs4`              | HTML parsing (BeautifulSoup)               |

---

## Development Notes

### Code Style
- Formatter: **Black**
- Linter: **Flake8** (`.flake8` config present)
- Static analysis: **DeepSource** + **Codacy**

### Testing
- Built-in test module at `heroku/modules/test.py`
- No dedicated test framework — testing is done via the Telegram bot interface

### Deployment Options
1. **VPS/VDS** — Direct Python installation (`python -m heroku`)
2. **Docker** — `docker-compose up -d` or `docker.sh`
3. **Hosted** — HikkaHost, Lavhost, Jamhost bots

### Environment Detection
The `heroku/utils/platform.py` module detects:
- WSL, Windows, Docker, Lavhost, Raspberry Pi, and generic Linux
- Used to adapt behavior and UI strings per platform

### Localization
- Language packs in `heroku/langpacks/*.yml`
- All user-facing strings go through `Translator`/`Strings`
- Supported: English, Russian, Ukrainian, German, Japanese
- Meme packs: 1337, Neofit, TikTok, UwU

### Backward Compatibility
- `heroku/compat/geek.py` transforms legacy GeekTG module code at load time
- Modules written for FTG, GeekTG, and Hikka work without modification

---

## Common Tasks for Agents

### Adding a new built-in module
1. Create `heroku/modules/<name>.py`
2. Define class `<Name>Mod(loader.Module)` with `strings = {"name": "..."}`
3. Add command handlers as `async def <cmd>cmd(self, message)`
4. The module auto-loads — no registration needed

### Modifying security permissions
- Edit `heroku/security.py` for permission bitmaps
- Edit `heroku/modules/heroku_security.py` for the user-facing security commands

### Adding a new language pack
1. Create `heroku/langpacks/<code>.yml` following the structure of `en.yml`
2. Register the language code in `heroku/translations.py`

### Modifying the Web UI
- Templates: `web-resources/*.jinja2`
- Static assets: `web-resources/static/`
- Backend routes: `heroku/web/root.py`
- Server lifecycle: `heroku/web/core.py`

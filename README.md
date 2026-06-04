# Progress-Course-Platform
#  Прогресс — ҰБТ Дайындық Курс Платформасы

> Математика және Информатика пәндерінен ҰБТ-ға дайындайтын онлайн платформа.

##  Жоба туралы

**Прогресс** — Қазақстан оқушыларына ҰБТ-ға дайындалуға арналған онлайн курс платформасы. Пайдаланушы тіркеліп, математика мен информатика курстарына қол жеткізеді. Бейнесабақтар, PDF материалдар және сынақ тапсырмалары — барлығы бір жерде.

##  Мүмкіндіктер

-  **Аутентификация** — Тіркелу, кіру, шығу
-  **Валидация** — Email форматы, құпия сөз күші, міндетті өрістер
-  **Курстар каталогы** — Іздеу, сүзгілеу, санат бойынша бөлу
-  **Бейнесабақтар** — YouTube сілтемелері арқылы
-  **Материалдар** — PDF, PPT жүктеулер
-  **Профиль беті** — Тіркелген курстар, аккаунт ақпараты
-  **Адаптивті дизайн** — Телефон, планшет, компьютер

##  Файл құрылымы

```
Progress-Course-Platform/
├── index.html          # Басты бет (landing page)
├── login.html          # Кіру беті
├── register.html       # Тіркелу беті
├── courses.html        # Курстар каталогы
├── course-detail.html  # Курс ішіндегі беті
├── profile.html        # Пайдаланушы профилі
└── README.md           # Осы файл
```

##  Деректер сақтау

Frontend ғана (localStorage) — Backend бөлімі жоқ (тапсырма талабынан тыс).

**Кестелер (localStorage keys):**
- `progress_users` — барлық тіркелген пайдаланушылар
- `progress_current_user` — ағымдағы кірген пайдаланушы

**Пайдаланушы объектісі:**
```json
{
  "id": 1234567890,
  "firstName": "Айдана",
  "lastName": "Серікова",
  "email": "aidana@example.com",
  "password": "base64_encoded",
  "phone": "+7 700 000 0000",
  "enrolledCourses": [1, 5],
  "createdAt": "2025-01-01T00:00:00.000Z"
}
```

##  Іске қосу

1. Репозиторийді клондаңыз:
```bash
git clone https://github.com/Sapa-Nuraiym/Progress-Course-Platform.git
cd Progress-Course-Platform
```

2. `index.html` файлын браузерде ашыңыз.

##  Байланыс

Сұрақтар үшін: **sapanuraiym@gmail.com**

---

##  Күнделікті жоспар (GitHub коммиттер)

| Күн | Тапсырма | Коммит хабары |
|-----|----------|---------------|
| **1-күн** | Жоба жоспарлау, репозиторий | `feat: project init, folder structure` |
| **2-күн** | Ортаны баптау, Git | `chore: gitignore, project structure setup` |
| **3-күн** | Дерекқор жобалау (ERD) | `docs: add database schema ERD` |
| **4-күн** | Деректер модельдерін жазу | `feat: localStorage data models, user schema` |
| **5-күн** | CRUD — Жазу, оқу | `feat: user register and login CRUD` |
| **6-күн** | Валидация және қауіпсіздік | `feat: form validation, email and password checks` |
| **7-күн** | Аутентификация жүйесі | `feat: auth system, session management` |
| **8-күн** | Курстар, профиль беті | `feat: courses page, profile page, enroll system` |
| **9-күн** | Дизайн жетілдіру | `style: final design polish, responsive fixes` |
| **10-күн** | README, деплой | `docs: README update, deploy to GitHub Pages` |

---

*© 2025 Прогресс — ҰБТ Дайындық Платформасы*

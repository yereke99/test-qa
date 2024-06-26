## 1.1 Чеклист тестирования заполнения формы на DemoQA
1.1. Валидация полей
Проверка заполнения полей "First Name", "Last Name", "Email", "Mobile Number", "Date of Birth", "Subjects", "Hobbies", "Address", и "State" с корректными данными.
Проверка заполнения полей с недопустимыми данными (например, пустые поля, неправильный формат даты рождения) и проверка, что форма не позволяет регистрацию пользователя с такими данными.

1.2. Валидация даты рождения
Проверка, что дата рождения может быть выбрана из календаря.
Проверка, что дата рождения может быть указана вручную в формате "DD/MM/YYYY".

1.3. Валидация выбора предметов
Проверка, что можно выбрать несколько предметов из списка.
Проверка, что можно выбрать только один предмет из списка.

1.4. Валидация выбора хобби
Проверка, что можно выбрать несколько хобби из списка.
Проверка, что можно выбрать только один хобби из списка.

1.5. Валидация адреса
Проверка, что можно ввести адрес в текстовое поле.
Проверка, что адрес может быть длиннее или короче заданного формата.


1.6. Валидация состояния
Проверка, что можно выбрать состояние из списка.
Проверка, что можно выбрать только один государство из списка.

1.7. Валидация кнопки "Submit"
Проверка, что кнопка "Submit" является активной и может быть нажата.
Проверка, что после нажатия кнопки "Submit" форма отправляется и отображается сообщение об успешной отправке.


## 1.2 Чеклист тестирования API Account на DemoQA
1.1. Валидация создания пользователя
Проверка, что API создает нового пользователя с корректными данными.
Проверка, что API не создает пользователя с недопустимыми данными (например, пустые поля, неправильный формат даты рождения).

1.2. Валидация получения пользователя
Проверка, что API возвращает информацию о существующем пользователе.
Проверка, что API не возвращает информацию о несуществующем пользователе.

1.3. Валидация обновления пользователя
Проверка, что API обновляет информацию о существующем пользователе.
Проверка, что API не обновляет информацию о несуществующем пользователе.

## 1.3 Чеклист тестирования калькулятора
1.1. Валидация арифметических операций
Проверка, что калькулятор выполняет сложение, вычитание, умножение, и деление с корректными числами.
Проверка, что калькулятор не выполняет операции с недопустимыми данными (например, деление на ноль).

1.2. Валидация ввода чисел
Проверка, что калькулятор принимает числа в различных форматах (например, целые, дробные, отрицательные).
Проверка, что калькулятор не принимает недопустимые данные (например, текст, символы).

1.3. Валидация ошибок и исключений
Проверка, что калькулятор отображает ошибки и исключения при выполнении операций с недопустимыми данными.
Проверка, что калькулятор не падает при выполнении операций с недопустимыми данными.

## 2.1 Тест кейсы для заполнения формы на DemoQA
1. **Тест-кейс 1: Валидация обязательных полей**
   - **Название**: Валидация обязательных полей
   - **Предусловие**: Открыта страница формы заполнения
   - **Действие**:
     - Ввести в поле "First Name" корректное имя
     - Ввести в поле "Last Name" корректное фамилию
     - Ввести в поле "Email" корректный электронный адрес
     - Ввести в поле "Mobile Number" корректный номер телефона
     - Ввести в поле "Date of Birth" корректную дату рождения
     - Ввести в поле "Subjects" корректный предмет
     - Ввести в поле "Hobbies" корректное хобби
     - Ввести в поле "Address" корректный адрес
     - Ввести в поле "State" корректное государство
   - **Ожидаемый результат**: Форма успешно заполнена, и пользователь может продолжить регистрацию.

2. **Тест-кейс 2: Валидация не обязательных полей**
   - **Название**: Валидация не обязательных полей
   - **Предусловие**: Открыта страница формы заполнения
   - **Действие**:
     - Ввести в поле "First Name" корректное имя
     - Ввести в поле "Last Name" корректную фамилию
     - Оставить поля "Email", "Mobile Number", "Date of Birth", "Subjects", "Hobbies", "Address", и "State" пустыми
   - **Ожидаемый результат**: Форма может быть отправлена, но поля "Email", "Mobile Number", "Date of Birth", "Subjects", "Hobbies", "Address", и "State" не заполнены.

3. **Тест-кейс 3: Валидация ошибок**
   - **Название**: Валидация ошибок
   - **Предусловие**: Открыта страница формы заполнения
   - **Действие**:
     - Ввести в поле "First Name" недопустимое имя
     - Ввести в поле "Last Name" недопустимую фамилию
     - Ввести в поле "Email" недопустимый электронный адрес
     - Ввести в поле "Mobile Number" недопустимый номер телефона
     - Ввести в поле "Date of Birth" недопустимую дату рождения
     - Ввести в поле "Subjects" недопустимый предмет
     - Ввести в поле "Hobbies" недопустимое хобби
     - Ввести в поле "Address" недопустимый адрес
     - Ввести в поле "State" недопустимое государство
   - **Ожидаемый результат**: Форма не может быть отправлена, и пользователь получает ошибки валидации.

## 2.2 Тест кейсы для API Account на DemoQA

1. **Тест-кейс 1: Создание пользователя**
   - **Название**: Создание пользователя
   - **Предусловие**: Открыта страница Swagger UI
   - **Действие**:
     - Отправить запрос POST на эндпоинт `/account` с корректными данными для создания пользователя
     - Проверить, что пользователь успешно создан
   - **Ожидаемый результат**: Новый пользователь создан, и информация о пользователе возвращается в ответе.

2. **Тест-кейс 2: Получение пользователя**
   - **Название**: Получение пользователя
   - **Предусловие**: Открыта страница Swagger UI
   - **Действие**:
     - Отправить запрос GET на эндпоинт `/account/{id}` с корректным идентификатором пользователя
     - Проверить, что информация о пользователе возвращается в ответе
   - **Ожидаемый результат**: Информация о пользователе возвращается в ответе.

3. **Тест-кейс 3: Обновление пользователя**
   - **Название**: Обновление пользователя
   - **Предусловие**: Открыта страница Swagger UI
   - **Действие**:
     - Отправить запрос PUT на эндпоинт `/account/{id}` с корректными данными для обновления пользователя
     - Проверить, что пользователь успешно обновлен
   - **Ожидаемый результат**: Пользователь обновлен, и информация о пользователе возвращается в ответе.

## 2.3 Тест кейсы для калькулятора

1. **Тест-кейс 1: Сложение двух чисел**
   - **Название**: Сложение двух чисел
   - **Предусловие**: Открыт калькулятор
   - **Действие**:
     - Ввести в поле "Number 1" число 5
     - Ввести в поле "Number 2" число 3
     - Нажать кнопку "Add"
     - Проверить, что результат равен 8
   - **Ожидаемый результат**: Результат сложения равен 8.

2. **Тест-кейс 2: Вычитание двух чисел**
   - **Название**: Вычитание двух чисел
   - **Предусловие**: Открыт калькулятор
   - **Действие**:
     - Ввести в поле "Number 1" число 10
     - Ввести в поле "Number 2" число 4
     - Нажать кнопку "Subtract"
     - Проверить, что результат равен 6
   - **Ожидаемый результат**: Результат вычитания равен 6.

3. **Тест-кейс 3: Ошибка при делении на ноль**
   - **Название**: Ошибка при делении на ноль
   - **Предусловие**: Открыт калькулятор
   - **Действие**:
     - Ввести в поле "Number 1" число 10
     - Ввести в поле "Number 2" число 0
     - Нажать кнопку "Divide"
   - **Ожидаемый результат**: Калькулятор отображает ошибку, что деление на ноль не допустимо.

## 3 Баг репорты

1. **Баг-репорт 1: Некорректное сложение отрицательных чисел**
   - **Описание**: Калькулятор неправильно обрабатывает сложение отрицательных чисел. Например, при сложении -5 и -3, результатом является 2, а ожидаемый результат -8.
   - **Шаги для воспроизведения**:
     - Открыть калькулятор
     - Ввести в поле "Number 1" число -5
     - Ввести в поле "Number 2" число -3
     - Нажать кнопку "Add"
     - Проверить результат
   - **Ожидаемый результат**: Результат сложения равен -8.
   - **Фактический результат**: Результат сложения равен 2.

2. **Баг-репорт 2: Некорректное вычитание отрицательных чисел**
   - **Описание**: Калькулятор неправильно обрабатывает вычитание отрицательных чисел. Например, при вычитании -5 из -3, результатом является 2, а ожидаемый результат -8.
   - **Шаги для воспроизведения**:
     - Открыть калькулятор
     - Ввести в поле "Number 1" число -3
     - Ввести в поле "Number 2" число -5
     - Нажать кнопку "Subtract"
     - Проверить результат
   - **Ожидаемый результат**: Результат вычитания равен -8.
   - **Фактический результат**: Результат вычитания равен 2.

3. **Баг-репорт 3: Некорректное деление на ноль**
   - **Описание**: Калькулятор не отображает ошибку при делении на ноль. Например, при делении 10 на 0, калькулятор не отображает ошибку, а вместо этого возвращает неопределенный результат.
   - **Шаги для воспроизведения**:
     - Открыть калькулятор
     - Ввести в поле "Number 1" число 10
     - Ввести в поле "Number 2" число 0
     - Нажать кнопку "Divide"
     - Проверить результат
   - **Ожидаемый результат**: Калькулятор отображает ошибку, что деление на ноль не допустимо.
   - **Фактический результат**: Калькулятор возвращает неопределенный результат.
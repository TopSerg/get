## Сборка проекта под Windows

1. Установите [Visual Studio 2022](https://visualstudio.microsoft.com/ru/downloads/).
2. Скачайте файл [VisualGDB-5.6r8_retail.msi](https://fost.ws/soft/visualgdb-5-6-r8-key-2023/?ysclid=m8cre3j7go885579343) и установите
3. Скачайте [Git](https://git-scm.com/downloads/win)/
4. Создайте рабочую папку и откройте там git command line
5. Введите команду для клонирования репозитория 

```git clone https://gitlab.com/on4ip84/controllerat32.git```

6. Перейдите в созданную папку с помощью команды

```cd controllerat32/```

7. Подгрузите подмодули из других репозиториев

```git submodule update --init --recursive```

8. Откройте файл AT32_Base.sln и соберите проект



## Возможные ошибки
Если видите ошибку attempt to rename spec ```'link' to already defined spec 'nano_link'```, то зайдите в файл stm32.props и удалите строку, содержащую: ```<AdditionalOptions>--specs=nano.specs --specs=nosys.specs -Wl,--no-warn-rwx-segments %(Link.AdditionalOptions)</AdditionalOptions>```

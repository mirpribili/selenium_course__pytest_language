# selenium_course__pytest_language
- pytest --language=es test_items.py
- pytest --language=fr test_items.py

<span><h2>Задание: запуск автотестов для&nbsp;разных языков&nbsp;интерфейса</h2>

<p>Мы хотим, чтобы разрабатываемый нами интернет-магазин работал одинаково хорошо для пользователей из любой страны. Чтобы убедиться в работоспособности решения с поддержкой разных языков, мы планируем запускать набор автотестов для каждого языка. Вам как разработчику автотестов нужно реализовать решение, которое позволит запускать автотесты для разных языков пользователей, передавая нужный язык в командной строке.</p>

<ol>
	<li>Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.</li>
	<li>Добавьте в&nbsp;файл&nbsp;conftest.py обработчик, который считывает из командной строки параметр language.</li>
	<li>Реализуйте в файле conftest.py логику&nbsp;запуска браузера с указанным&nbsp;языком пользователя. Браузер должен объявляться в фикстуре browser&nbsp;и передаваться в тест как параметр.</li>
	<li>В файл test_items.py напишите тест, который проверяет, что&nbsp;страница&nbsp;товара на сайте содержит&nbsp;кнопку&nbsp;добавления в корзину. Например, можно проверять&nbsp;товар, доступный по&nbsp;<a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" rel="noopener noreferrer nofollow" target="_blank">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/</a>.</li>
	<li>Тест должен запускаться&nbsp;с параметром language следующей командой:</li>
	**pytest --language=es test_items.py**
	<li>и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.</li>
	<li>Отправить ссылку на данный репозиторий в качестве ответа на данное задание.</li>
	<li>Отправить решение на рецензирование другим учащимся. Не забудьте, что решение на рецензирование можно отправить только один раз.</li>
	<li>Проверьте решения&nbsp;минимум трех других учащихся, чтобы получить баллы за задание.</li>
</ol>

<p>Это задание с peer-review, поэтому кроме формальных критериев другие учащиеся могут проверять корректность написания вашего кода.&nbsp;</p>

<p>Важно! Если при рецензировании чужого решения вы получаете ошибку вроде:&nbsp;</p>

<pre><code class="hljs puppet">raise ValueError(<span class="hljs-string"><span class="hljs-string">"option names %s already added"</span></span> % conflict)

ValueError: option <span class="hljs-keyword"><span class="hljs-keyword">names</span></span> {<span class="hljs-string"><span class="hljs-string">'--language'</span></span>} <span class="hljs-keyword"><span class="hljs-keyword">already</span></span> <span class="hljs-keyword"><span class="hljs-keyword">added</span></span></code></pre>

<p>Перепроверьте, что у вас нет своего conftest.py в директории выше, смотри <a href="/lesson/237240/step/4?unit=209628" rel="noopener noreferrer nofollow">шаг 4</a>.</p>

<p>&nbsp;</p>

<p>Ваше решение будет проверяться по следующим критериям:</p>

<ol>
	<li>Тест в репозитории можно запустить командой <code>pytest --language=es</code>, тест успешно проходит.</li>
	<li>Проверка работоспособности кода для разных языков. Добавьте в файл с тестом команду<strong> time.sleep(30)</strong> сразу после открытия ссылки. Запустите тест с параметром <strong>--language=fr&nbsp;</strong>и визуально проверьте, что фраза на кнопке добавления в корзину выглядит так: <strong>"Ajouter au panier"</strong>.</li>
	<li>Браузер должен объявляться в фикстуре <strong>browser</strong> и передаваться в тест как параметр.</li>
	<li>В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным для проверяемой страницы. <u>Есть <strong>assert</strong>.</u></li>
	<li>Название тестового метода внутри файла test_items.py соответствует задаче. Название test_something не удовлетворяет требованиям.</li>
</ol>

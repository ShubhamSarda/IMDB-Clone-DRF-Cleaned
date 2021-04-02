# IMDB API Clone With DRF

<h3>🔗 Final Project Links (Arranged According To Usage)</h3>
<br>

<b>1. Admin Access</b>
<ul>
    <li>Admin Section: http://127.0.0.1:8000/dashboard/</li>
</ul>
<br>

<b>2. Accounts</b>
<ul>
    <li>Registration: http://127.0.0.1:8000/api/account/register/</li>
    <li>Login: http://127.0.0.1:8000/api/account/login/</li>
    <li>Logout: http://127.0.0.1:8000/api/account/logout/</li>
</ul>
<br>

<b>3. Stream Platforms</b>
<ul>
    <li>Create Element & Access List: http://127.0.0.1:8000/api/watch/stream/</li>
    <li>Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/stream/<int:streamplatform_id>/</li>

</ul>
<br>

<b>4. Watch List</b>
<ul>
    <li>Create & Access List: http://127.0.0.1:8000/api/watch/</li>
    <li>Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/watch/<int:movie_id>/</li>
</ul>
<br>

<b>5. Reviews</b>
<ul>
    <li>Create Review For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/create/</li>
    <li>List Of All Reviews For Specific Movie: http://127.0.0.1:8000/api/watch/<int:movie_id>/reviews/</li>
    <li>Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/watch/reviews/<int:review_id>/</li>
</ul>
<br>

<b>6. User Review</b>
<ul>
    <li>Access All Reviews For Specific User: http://127.0.0.1:8000/api/watch/user-reviews/?username=example</li>
</ul>
<br>
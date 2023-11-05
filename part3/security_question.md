# what would you look for to make your system secure?

Regarding to the MySQL database, I would look for SQL Injection vulnerabilities,
some implementations would handle SQL queries as implicit strings that can contain
malicious characters that scape desired SQL commands and execute additional commands,
both active such as DROP, DELETE or passive such as SELECT over INFORMATION_SCHEMA or even
SELECT over tables that contain sensitive information, as said, passwords, users addresses, etc

In order to prevent such vulnerabilities, SQL queries should be handled by ORMs or prepared
statements where we are able to define the query structure and the parameters that will be
used in the query, preventing the injection of undesired and unscaped characters.

We've talked before about passwords saved in the database, one concern that must be considered
as critical must be to Hash passwords by means of "secure" algorithms such as SHA-256 or even
SHA-512 (here performance can be also be taken into account). The relevance of hashing passwords
falls in the fact that, if a database gets compromised (as mentioned before, due to SQL Injection or
a similar attack), cleartext passwords would be exposed and be directly usable by the attacker to
impersonate users in the system. Also it is recommendable to add advanced hashing features such as random 
salts that make it more difficult to crack passwords by means of cryptographic techniques based
on SHA's mathematical basis (as happened with MD5, an older hashing algorithm that has been proven to be
vulnerable via computational algorithms). Finally it is also recommendable to be aware of the current
algorithm updates since there are trials to break SHA algorithms by means of quantum computing methods.

In other side, mobile devices such as Android and IOs and even desktop devices can be vulnerable to attacks 
that involve the installation of malicious apps / programs (phishing, trojans, keyloggers, etc) that can
access user's auth, localizations, configurations, etc, it is recommendable to use device hardening techniques
such as the use of antivirus and scanning software to detect risks early enough to take proper actions.

As a side note, since mentioned web frontend is made using Javascript and Next JS there is a risk of Javascript
Script Injection attaacks that executes code in user's web browser. Such attacks could extract LocalStorage variables
(in example, auth tokens) and send them to a malicious server that collects such info to impersonate users while performing
transactions.

Furthermore, having a monolithic architecture implemented in FastAPI would be vulnerable against DDoS attacks since a single 
execution component would receive all of the fake requests. Note that such component could be scalated in order to ensure
system availability, however scaling a monolith is not as profitable as having separated tiers for both frontend and backend 
components.

In addition, having 12 employees with full access to all of system resources is considered a bad practice, a least
privilege principle approach must be taken in such way engineers (and any class of employee) have access to only
the resources they need to perform their tasks, for example, a software engineer should have access to a previously 
prepared development / testing environment that is not directly linked to deployment env, this also applies to customer
support employees, even through they are allowed to see user's personal data, they shouldn't be able to create, edit
or delete such data with whole freedom, there must be customized policies and restrictions that apply to certain
groups of user's personal, transactions and orders data, for example, requiring a customer support employee to 
open a request before performing an artificial change to user's registry of orders. Also an accounting strategy must be
implemented in such way employees actions are recorded and prevent actions repudiation events.

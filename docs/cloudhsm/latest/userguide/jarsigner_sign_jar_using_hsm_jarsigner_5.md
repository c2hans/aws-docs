---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/jarsigner_sign_jar_using_hsm_jarsigner_5.html
---

# Sign a JAR file using AWS CloudHSM and Jarsigner
<a name="jarsigner_sign_jar_using_hsm_jarsigner_5"></a>

Use the following command to sign a JAR file using AWS CloudHSM and Jarsigner:

------
#### [ Linux; ]

For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -keystore example_keystore.store \
	-signedjar signthisclass_signed.jar \
	-sigalg sha512withrsa \
	-storetype CloudHSM \
	-J-classpath '-J/opt/cloudhsm/java/*' \
	-J-Djava.library.path=/opt/cloudhsm/lib \
	signthisclass.jar {{<key pair label>}}
```

------
#### [ Windows ]

For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -keystore example_keystore.store `
	-signedjar signthisclass_signed.jar `
	-sigalg sha512withrsa `
	-storetype CloudHSM `
	-J-classpath '-JC:\Program Files\Amazon\CloudHSM\java\*'`
	 "-J-Djava.library.path='C:\Program Files\Amazon\CloudHSM\lib\'" `
	signthisclass.jar {{<key pair label>}}
```

------

Use the following command to verify a signed JAR:

------
#### [ Linux ]

For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -verify \
	-keystore example_keystore.store \
	-sigalg sha512withrsa \
	-storetype CloudHSM \
	-J-classpath '-J/opt/cloudhsm/java/*' \
	-J-Djava.library.path=/opt/cloudhsm/lib \
	signthisclass_signed.jar {{<key pair label>}}
```

------
#### [ Windows ]

For OpenJDK 17, OpenJDK 21, and OpenJDK 25

```
jarsigner -verify `
	-keystore example_keystore.store `
	-sigalg sha512withrsa `
	-storetype CloudHSM `
	-J-classpath '-JC:\Program Files\Amazon\CloudHSM\java\*'`
	"-J-Djava.library.path='C:\Program Files\Amazon\CloudHSM\lib\'" `
	signthisclass_signed.jar {{<key pair label>}}
```

------

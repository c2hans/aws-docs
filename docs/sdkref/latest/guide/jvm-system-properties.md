---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/jvm-system-properties.html
---

# Using JVM system properties to globally configure AWS SDK for Java and AWS SDK for Kotlin
<a name="jvm-system-properties"></a>

[JVM system properties](https://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html) provide another way to specify configuration options and credentials for SDKs that run on the JVM such as the AWS SDK for Java and the AWS SDK for Kotlin. For a list of JVM system properties supported by SDKs, see [Settings reference](settings-reference.md#JVMSettings).

**Precedence of options**
+ If you specify a setting by using its JVM system property, it overrides any value found in environment variables or loaded from a profile in the shared AWS `config` and `credentials` files.
+ If you specify a setting by using its environment variable, it overrides any value loaded from a profile in the shared AWS `config` and `credentials` files.

## How to set JVM system properties
<a name="jvm-sys-props-set"></a>

You can set JVM system properties several ways.

### On the command line
<a name="jvm-sys-props-set-cl"></a>

Set JVM system properties on the command-line when invoking the `java` command by using the `-D` switch. The following command configures the AWS Region globally for all service clients unless you explicitly override the value in code.

```
java -Daws.region=us-east-1 -jar <your_application.jar> <other_arguments>
```

If you need to set multiple JVM system properties, specify the `-D` switch multiple times.

### With an environment variable
<a name="jvm-sys-props-set-evar"></a>

If you can't access the command line to invoke the JVM to run your application, you can use the `JAVA_TOOL_OPTIONS` environment variable to configure command-line options. This approach is useful in situations such as running an AWS Lambda function on the Java runtime or running code in an embedded JVM.

The following example configures the AWS Region globally for all service clients unless you explicitly override the value in code.

------
#### [ Linux, macOS, or Unix ]

```
$ export JAVA_TOOL_OPTIONS={{"-Daws.region=us-east-1"}}
```

Setting the environment variable changes the value used until the end of your shell session, or until you set the variable to a different value. You can make the variables persistent across future sessions by setting them in your shell's startup script.

------
#### [ Windows Command Prompt ]

```
C:\> setx JAVA_TOOL_OPTIONS {{-Daws.region=us-east-1}}
```

Using `[set](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/set_1)` to set an environment variable changes the value used until the end of the current Command Prompt session, or until you set the variable to a different value. Using [https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/setx](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/setx) to set an environment variable changes the value used in both the current Command Prompt session and all Command Prompt sessions that you create after running the command. It does ***not*** affect other command shells that are already running at the time you run the command.

------

### At runtime
<a name="jvm-sys-props-set-runtime"></a>

You can also set JVM system properties at runtime in code by using the `System.setProperty` method as shown in the following example.

```
System.setProperty("aws.region", "us-east-1");
```

**Important**
Set any JVM system properties *before* you initialize SDK service clients, otherwise service clients may use other values.

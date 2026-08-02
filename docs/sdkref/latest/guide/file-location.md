---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/file-location.html
---

# Finding and changing the location of the shared `config` and `credentials` files of AWS SDKs and tools
<a name="file-location"></a>

The shared AWS `config` and `credentials` files are plaintext files that hold configuration information for the AWS SDKs and tools. The files reside locally in your environment and used automatically by SDK code or by AWS CLI commands that you run in that environment. For example, on your own computer or when developing on an Amazon Elastic Compute Cloud instance.

When the SDK or tool runs, it checks for these files and loads any available configuration settings. If the files do not already exist, then a basic file is automatically created by the SDK or tool.

By default, the files are in a folder named `.aws` that is placed in your `home` or user folder.

| Operating system | Default location and name of files |
| --- | --- |
| Linux and macOS | `~/.aws/config`<br />`~/.aws/credentials` |
| Windows | `%USERPROFILE%\.aws\config`<br />`%USERPROFILE%\.aws\credentials` |

## Home directory resolution
<a name="homeDirRes"></a>

`~` is only used for home directory resolution when it:
+ Starts the path
+ Is followed immediately by `/` or a platform specific separator. On windows, `~/` and `~\` both resolve to the home directory.

When determining the home directory, the following variables are checked:
+ (All platforms) The `HOME` environment variable
+ (Windows platforms) The `USERPROFILE` environment variable
+ (Windows platforms) The concatenation of `HOMEDRIVE` and `HOMEPATH` environment variables (`$HOMEDRIVE$HOMEPATH`)
+ (Optional per SDK or tool) An SDK or tool-specific home path resolution function or variable

When possible, if a user's home directory is specified at the start of the path (for example, `~username/`), it is resolved to the requested user name's home directory (for example, `/home/username/.aws/config`).

## Change the default location of these files
<a name="file-location-change"></a>

You can use any of the following to override where these files are loaded from by the SDK or tool.

### Use environment variables
<a name="file-location-change-envar"></a>

The following environment variables can be set to change the location or name of these files from the default to a custom value:
+ `config` file environment variable: **`AWS_CONFIG_FILE`**
+ `credentials` file environment variable: **`AWS_SHARED_CREDENTIALS_FILE`**

------
#### [ Linux/macOS ]

You can specify an alternate location by running the following [export](https://linuxconfig.org/learning-linux-commands-export) commands on Linux or macOS.

```
$ export AWS_CONFIG_FILE=/some/file/path/on/the/system/config-file-name
$ export AWS_SHARED_CREDENTIALS_FILE=/some/other/file/path/on/the/system/credentials-file-name
```

------
#### [ Windows ]

You can specify an alternate location by running the following [setx](https://docs.microsoft.com/windows-server/administration/windows-commands/setx) commands on Windows.

```
C:\> setx AWS_CONFIG_FILE c:\some\file\path\on\the\system\config-file-name
C:\> setx AWS_SHARED_CREDENTIALS_FILE c:\some\other\file\path\on\the\system\credentials-file-name
```

------

For more information on configuring your system using environment variables, see [Using environment variables to globally configure AWS SDKs and tools](environment-variables.md).

### Use JVM system properties
<a name="file-location-change-jvmSysProp"></a>

For the SDK for Kotlin running on the JVM and for SDK for Java 2.x, you can set the following JVM system properties to change the location or name of these files from the default to a custom value:
+ `config` file JVM system property: **`aws.configFile`**
+ `credentials` file environment variable: **`aws.sharedCredentialsFile`**

For instructions on how to set JVM system properties, see [How to set JVM system properties](jvm-system-properties.md#jvm-sys-props-set). The SDK for Java 1.x does not support these system properties.

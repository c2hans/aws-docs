---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/keystore-prerequisites.html
---

# Prerequisites for integrating AWS CloudHSM with Java Keytool and Jarsigner using Client SDK 3
<a name="keystore-prerequisites"></a>

To use the AWS CloudHSM key store, you must first initialize and configure the AWS CloudHSM JCE SDK. Use the following steps to do so.

## Step 1: Install the JCE
<a name="prereq-step-one"></a>

To install the JCE, including the AWS CloudHSM client prerequisites, follow the steps for [installing the Java library](java-library-install.md).

## Step 2: Add HSM login credentials to environment variables
<a name="prereq-step-two"></a>

Set up environment variables to contain your HSM login credentials.

```
export HSM_PARTITION=PARTITION_1
export HSM_USER={{<HSM user name>}}
export HSM_PASSWORD={{<HSM password>}}
```

**Note**
The CloudHSM JCE offers various login options. To use the AWS CloudHSM key store with third-party applications, you must use implicit login with environment variables. If you want to use explicit login through application code, you must build your own application using the AWS CloudHSM key store. For additional information, see the article on [Using AWS CloudHSM Key Store](alternative-keystore.md).

## Step 3: Register the JCE provider
<a name="prereq-step-three"></a>

To register the JCE provider, in the Java CloudProvider configuration.

1. Open the java.security configuration file in your Java installation, for editing.

1. In the java.security configuration file, add `com.cavium.provider.CaviumProvider` as the last provider. For example, if there are nine providers in the java.security file, add the following provider as the last provider in the section. Adding the Cavium provider as a higher priority may negatively impact your system's performance.

   `security.provider.10=com.cavium.provider.CaviumProvider`
**Note**
Power users may be accustomed to specifying `-providerName`, `-providerclass`, and `-providerpath` command line options when using keytool, instead of updating the security configuration file. If you attempt to specify command line options when generating keys with AWS CloudHSM key store, it will cause errors.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

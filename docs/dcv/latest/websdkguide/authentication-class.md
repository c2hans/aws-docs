---
source_url: https://docs.aws.amazon.com/dcv/latest/websdkguide/authentication-class.html
---

# Authentication Class
<a name="authentication-class"></a>

The Authentication Class must be used to obtain an authentication token by calling the [`authenticate` method](dcv-module.md#authenticate) of the `dcv` module. For an example showing how to use it, see the [Getting started](establish-connection.md#auth-conn) section.

**Topics**
+ [Methods](#methods)

## Methods
<a name="methods"></a>

**Topics**
+ [retry() → {void}](#retry)
+ [sendCredentials(credentials) → {void}](#sendCredentials)

### retry() → {void}
<a name="retry"></a>

 Retries the authentication process.

#### Returns:
<a name="returns"></a>

 Type
 void

### sendCredentials(credentials) → {void}
<a name="sendCredentials"></a>

 Sends the authentication credentials provided by the client to the Amazon DCV server.

#### Parameters:
<a name="parameters-1"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  credentials  |  Object  |  The object containing the supplied credentials. The credentials must have the same name and be of the same type that is specified in the challenge.  |

#### Returns:
<a name="returns-1"></a>

 Type
 void

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

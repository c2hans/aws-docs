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

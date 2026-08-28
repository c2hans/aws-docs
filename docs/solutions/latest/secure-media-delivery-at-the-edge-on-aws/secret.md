---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/secret.html
---

# Secret
<a name="secret"></a>

*Object Properties*

**keys: object** an object holding primary and secondary key pairs for each instance. Structure of this object must conform with the following format:

```
{
    'primary': {
      'uuid': primary_key_uuid: string,
      'value': primary_key_value: string
    },
    'secondary': {
      'uuid': secondary_key_key: string
      'value': secondary_key_value: string
    }
}
```

 It is mandatory that any function used for retrieving signing keys return keys object in this exact form.

**ttl:** `[int]` → time to live expressed in seconds, detailing for how long keys should be considered as valid after they were retrieved. If the TTL expired, a new call to retrieve the keys will be invoked.

**retrieveMode**: `[string] = [‘native|’custom’] (default ‘native’)` → determines what function is used to retrieve the keys. native refers to the internal method which interacts with Secrets Manager to retrieve the secrets storing primary and secondary keys.

**retrieveFunction:** `[function] (default null)` → a reference to the function provided by the user, that is called when key needs to be retrieved. It is only used when **retrieveMode** is set to `custom`. The custom function must return object of the same structure as specified in **keys** property.

 **retrieveFunctionArgs:** `[array] (default [])` → stores positional arguments passed as input parameters when **retrieveFunction** is called.

 **stackName:** `[string] (default: null)` → stores the name of the deployed stack. In native mode of retrieval, it is required to derive Secrets Manager secrets name, which is: `{stack_name}_PrimarySecret` and `{stack_name}_SecondarySecret`. stackName value binds the key retrieval process with the specific stack’s secrets.

*Constructor*

**Secret(stackName: string, ttl: int, retrieveMode: string = ‘native’, retrieveFunction: string = null, retrieveFunctionArgs: array = []) →** constructor function maps the provided input to the object attributes

*Instance Methods*

**getKeyValue(key\_alias: string)** *returns: string →* returns the value of the specified key alias, either `primary` or `secondary`

**getKeyUUID(*key\_alias: string*)** *returns: string →* returns the UUID of the specified key alias, either primary or secondary

**initSMClient({region: string, role: string, profile: string})** *returns: Boolean* → using provided inputs a new Secrets Manager client is created using the adequate credentials. Execution role will be derived as follows:
+  If no role or profile was provided as an input, AWS SDK will determine which role to assume by following the standard process - it will look into environment variables, service execution role as described in [Setting Credentials in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-credentials-node.html).
+  If profile attribute was provided – use the credentials associated with it.
+  If no profile attribute was provided except iam\_role- assume iam\_role through AWS Security Token Service (AWS STS).

 If the Region was not specified in the input object, AWS SDK provided method is used to verify what is the default region for the active profile. If none is specified, we default to `us-east-1`. This function is used when **retrieveMode** is set to `native`. Returns `true` if the client set up is successful, or `false` if it fails.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

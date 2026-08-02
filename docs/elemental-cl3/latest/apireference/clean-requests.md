---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/clean-requests.html
---

# “Clean” Requests
<a name="clean-requests"></a>

A quick way to prepare the body for a new POST is to do a GET on an existing entity, and include the clean parameter in the request.With this parameter set to `true`, the GET response omits the <id> elements and other elements such as <status>, <service\_name>, and <service\_provider\_name> that do not apply to a POST.

1. Append `?clean=true` to the GET command. For example:

   ```
   GET http://101.4.136.95/profiles/2.xml?clean=true
   ```

1. Modify the response as desired and paste the revision in the body of the desired POST request.

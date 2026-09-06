---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/apireference/header-content-standard.html
---

# Header Content - Standard Elements
<a name="header-content-standard"></a>

For All Requests
+ Accept: Set to application/xml

For PUT and POST Requests
+ Accept: Set to application/xml
+ Content-Type: Set to application/xml

  When POSTing xml for a profile originally created with an earlier version of Conductor Live , set content-type to application/vnd.elemental\+xml;version=n.n.n, where n.n.n is the number of the Conductor Live version used to create the profile. For example, if the profile was created with Conductor Live version 3.2.1, use:

  ```
  content-type: application/vnd.elemental+xml;version=3.2.1
  ```

  For more information on using profiles created with earlier software versions, see [Versioning](versioning.md).

---
source_url: https://docs.aws.amazon.com/dcv/latest/extsdkguide/extension.executable.html
---

# Extension executable
<a name="extension.executable"></a>

Extension manifest files define the `executable` file spawned by Amazon DCV. Amazon DCV will exchange messages with the extension using the `stdin` and `stdout` of the extension process.
+ The Amazon DCV client starts the extension once a Amazon DCV connection is established. The executable runs in the context of the user who launched the client.
+ The Amazon DCV server starts the extension when a user logs in. The executable runs in the context of the logged-in user.

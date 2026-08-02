---
source_url: https://docs.aws.amazon.com/freertos/latest/userguide/configure-idt-sample.html
---

# Configure device information for IDT
<a name="configure-idt-sample"></a>

Configure your device information for IDT to run the test. You must update the `device.json` template located in the `{{<device-tester-extract-location>}}/configs` folder with the following information.

```
[
  {
    "id": "pool",
    "sku": "N/A",
    "devices": [
      {
        "id": "{{<device-id>}}",
        "connectivity": {
          "protocol": "ssh",
          "ip": "{{<ip-address>}}",
          "port": "{{<port>}}",
          "auth": {
            "method": "pki | password",
            "credentials": {
              "user": "{{<user-name>}}",
              "privKeyPath": "{{/path/to/private/key}}",
              "password": "{{<password>}}"
            }
          }
        }
      }
    ]
  }
]
```

In the `devices` object, provide the following information:

**`id`**
A user-defined unique identifier for your device.

**`connectivity.ip`**
The IP address of your device.

**`connectivity.port`**
Optional. The port number to use for SSH connections to your device.

**`connectivity.auth`**
Authentication information for the connection.
This property applies only if `connectivity.protocol` is set to `ssh`.
**`connectivity.auth.method`**
The authentication method used to access a device over the given connectivity protocol.
Supported values are:
+ `pki`
+ `password`
**`connectivity.auth.credentials`**
The credentials used for authentication.
**`connectivity.auth.credentials.user`**
The user name used to sign in to your device.
**`connectivity.auth.credentials.privKeyPath`**
The full path to the private key used to sign in to your device.
This value applies only if `connectivity.auth.method` is set to `pki`.
**`devices.connectivity.auth.credentials.password`**
The password used for signing in to your device.
This value applies only if `connectivity.auth.method` is set to `password`.

**Note**
Specify `privKeyPath` only if `method` is set to `pki`.
Specify `password` only if `method` is set to `password`.

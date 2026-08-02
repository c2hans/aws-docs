---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/jvm-ttl-dns.html
---

# Set the JVM TTL for DNS name lookups
<a name="jvm-ttl-dns"></a>

The Java virtual machine (JVM) caches DNS name lookups. When the JVM resolves a hostname to an IP address, it caches the IP address for a specified period of time, known as the *time-to-live* (TTL).

Because AWS resources use DNS name entries that occasionally change, we recommend that you configure your JVM with a TTL value of 5 seconds. This ensures that when a resource’s IP address changes, your application will be able to receive and use the resource’s new IP address by requerying the DNS.

On some Java configurations, the JVM default TTL is set so that it will *never* refresh DNS entries until the JVM is restarted. Thus, if the IP address for an AWS resource changes while your application is still running, it won’t be able to use that resource until you *manually restart* the JVM and the cached IP information is refreshed. In this case, it’s crucial to set the JVM’s TTL so that it will periodically refresh its cached IP information.

## How to set the JVM TTL
<a name="how-to-set-the-jvm-ttl"></a>

To modify the JVM’s TTL, set the [networkaddress.cache.ttl](https://docs.oracle.com/en/java/javase/17/core/java-networking.html#GUID-A680DADB-C4C1-40F1-B568-D9A97C917F5D) security property value. Note that `networkaddress.cache.ttl` is a *security property*, not a system property, i.e., it cannot be set with the `-D` command-line flag.

### Option 1: Set it programmatically in your application
<a name="set-ttl-programmatically"></a>

Call [https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/security/Security.html](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/security/Security.html) early in your application startup, before any AWS SDK clients are created and before any network requests are made:

```
import java.security.Security;

public class MyApplication {
    public static void main(String[] args) {
        Security.setProperty("networkaddress.cache.ttl", "5");

        // ... create SDK clients and run application
    }
}
```

### Option 2: Set it in the java.security file
<a name="set-ttl-java-security-file"></a>

Set the `networkaddress.cache.ttl` property in the `$JAVA_HOME/jre/lib/security/java.security` file for Java 8 or `$JAVA_HOME/conf/security/java.security` file for Java 11 or higher.

The following is a snippet from a `java.security` file that shows the TTL cache set to 5 seconds.

```
#
# The Java-level namelookup cache policy for successful lookups:
#
# any negative value: caching forever
# any positive value: the number of seconds to cache an address for
# zero: do not cache
#
...
{{networkaddress.cache.ttl=5}}
...
```

All applications that run on the JVM represented by the `$JAVA_HOME` environment variable use this setting.

### Option 3: Use the JDK system properties fallback (command-line)
<a name="set-ttl-system-property"></a>

If you cannot modify the security configuration or code, you can use JDK system properties. These act as fallbacks if no security property is defined.
+ `sun.net.inetaddr.ttl` – Controls successful lookups (positive TTL)
+ `sun.net.inetaddr.negative.ttl` – Controls failed lookups (negative TTL)

```
java -Dsun.net.inetaddr.ttl=5 -Dsun.net.inetaddr.negative.ttl=1 -jar myapp.jar
```

**Note**
These are JDK-internal properties documented in the [Oracle Java 8 Networking Properties](https://docs.oracle.com/javase/8/docs/technotes/guides/net/properties.html) reference as private properties that "may not be supported in future releases". Use Options 1-2 when possible.

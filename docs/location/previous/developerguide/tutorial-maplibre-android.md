---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tutorial-maplibre-android.html
---

# Using the MapLibre Native SDK for Android with Amazon Location Service
<a name="tutorial-maplibre-android"></a>

Use [MapLibre Native](https://github.com/maplibre/maplibre-gl-native) SDK to embed interactive maps into your Android applications.

The MapLibre Native SDK for Android is a library based on[ Mapbox Native](https://github.com/mapbox/mapbox-gl-native), and is compatible with the styles and tiles provided by the Amazon Location Service Maps API. You can integrate MapLibre Native SDK for Android to embed interactive map views with scalable, customizable vector maps in your Android applications.

This tutorial describes how to integrate the MapLibre Native SDK for Android with Amazon Location. The sample application for this tutorial is available as part of the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).

## Building the application: Initialization
<a name="tutorial-maplibre-android-initialization"></a>

To initialize your application:

1. Create a new Android Studio project from the **Empty Activity** template.

1. Ensure that **Kotlin** is selected for the project language.

1. Select a **Minimum SDK of API 14: Android 4.0 (Ice Cream Sandwich)** or newer.

1. Open **Project Structure**, then go to **File** > **Project Structure...** to choose the **Dependencies** section.

1. With **<All Modules>** selected,then choose the **\+** button to add a new **Library Dependency**.

1. Add **AWS Android SDK** version 2.20.0 or later. For example: `com.amazonaws:aws-android-sdk-core:2.20.0`

1. Add the **MapLibre Native SDK for Android** version 9.4.0 or later. For example: `org.maplibre.gl:android-sdk:9.4.0`

1. At the project level of your **build.gradle** file, add the following maven repository to access the MapLibre packages for Android:

   ```
   allprojects {
       repositories {
           // Retain your existing repositories
           google()
           jcenter()

           //  Declare the repositories for MapLibre
           mavenCentral()
       }
   }
   ```

## Building the application: Configuration
<a name="tutorial-maplibre-android-configuration"></a>

To configure your application with your resources and AWS Region:   Create `app/src/main/res/values/configuration.xml`.   Enter the names and identifiers of your resource the AWS Region they were created in:

```
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="identityPoolId">{{us-east-1:54f2ba88-9390-498d-aaa5-0d97fb7ca3bd}}</string>
    <string name="mapName">{{ExampleMap}}</string>
    <string name="awsRegion">{{us-east-1}}</string>
</resources>
```

## Building the application: Activity layout
<a name="tutorial-maplibre-android-activity-layout"></a>

Edit `app/src/main/res/layout/activity_main.xml`:
+ Add a `MapView`, which renders the map. This will also set the map's initial center point.
+ Add a `TextView`, which displays attribution.

```
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <com.mapbox.mapboxsdk.maps.MapView
        android:id="@+id/mapView"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        app:mapbox_cameraTargetLat="49.2819"
        app:mapbox_cameraTargetLng="-123.1187"
        app:mapbox_cameraZoom="12"
        app:mapbox_uiAttribution="false"
        app:mapbox_uiLogo="false" />

    <TextView
        android:id="@+id/attributionView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:background="#80808080"
        android:padding="5sp"
        android:textColor="@android:color/black"
        android:textSize="10sp"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        tools:ignore="SmallSp" />
</androidx.constraintlayout.widget.ConstraintLayout>
```

**Note**
You must provide word mark or text attribution for each data provider that you use, either on your application or your documentation. Attribution strings are included in the style descriptor response under the `sources.esri.attribution`, `sources.here.attribution`, and `source.grabmaptiles.attribution` keys. When using Amazon Location resources with [data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html), make sure to read the [service terms and conditions](https://aws.amazon.com/service-terms/).

## Building the application: Request transformation
<a name="tutorial-maplibre-android-request-transformation"></a>

Create a class named `SigV4Interceptor` to intercept AWS requests and sign them using [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). This will be registered with the HTTP client used to fetch map resources when the Main Activity is created.

```
package aws.location.demo.okhttp

import com.amazonaws.DefaultRequest
import com.amazonaws.auth.AWS4Signer
import com.amazonaws.auth.AWSCredentialsProvider
import com.amazonaws.http.HttpMethodName
import com.amazonaws.util.IOUtils
import okhttp3.HttpUrl
import okhttp3.Interceptor
import okhttp3.Request
import okhttp3.Response
import okio.Buffer
import java.io.ByteArrayInputStream
import java.net.URI

class SigV4Interceptor(
    private val credentialsProvider: AWSCredentialsProvider,
    private val serviceName: String
) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val originalRequest = chain.request()

        if (originalRequest.url().host().contains("amazonaws.com")) {
            val signer = if (originalRequest.url().encodedPath().contains("@")) {
                // the presence of "@" indicates that it doesn't need to be double URL-encoded
                AWS4Signer(false)
            } else {
                AWS4Signer()
            }

            val awsRequest = toAWSRequest(originalRequest, serviceName)
            signer.setServiceName(serviceName)
            signer.sign(awsRequest, credentialsProvider.credentials)

            return chain.proceed(toSignedOkHttpRequest(awsRequest, originalRequest))
        }

        return chain.proceed(originalRequest)
    }

    companion object {
        fun toAWSRequest(request: Request, serviceName: String): DefaultRequest<Any> {
            // clone the request (AWS-style) so that it can be populated with credentials
            val dr = DefaultRequest<Any>(serviceName)

            // copy request info
            dr.httpMethod = HttpMethodName.valueOf(request.method())
            with(request.url()) {
                dr.resourcePath = uri().path
                dr.endpoint = URI.create("${scheme()}://${host()}")

                // copy parameters
                for (p in queryParameterNames()) {
                    if (p != "") {
                        dr.addParameter(p, queryParameter(p))
                    }
                }
            }

            // copy headers
            for (h in request.headers().names()) {
                dr.addHeader(h, request.header(h))
            }

            // copy the request body
            val bodyBytes = request.body()?.let { body ->
                val buffer = Buffer()
                body.writeTo(buffer)
                IOUtils.toByteArray(buffer.inputStream())
            }

            dr.content = ByteArrayInputStream(bodyBytes ?: ByteArray(0))

            return dr
        }

        fun toSignedOkHttpRequest(
            awsRequest: DefaultRequest<Any>,
            originalRequest: Request
        ): Request {
            // copy signed request back into an OkHttp Request
            val builder = Request.Builder()

            // copy headers from the signed request
            for ((k, v) in awsRequest.headers) {
                builder.addHeader(k, v)
            }

            // start building an HttpUrl
            val urlBuilder = HttpUrl.Builder()
                .host(awsRequest.endpoint.host)
                .scheme(awsRequest.endpoint.scheme)
                .encodedPath(awsRequest.resourcePath)

            // copy parameters from the signed request
            for ((k, v) in awsRequest.parameters) {
                urlBuilder.addQueryParameter(k, v)
            }

            return builder.url(urlBuilder.build())
                .method(originalRequest.method(), originalRequest.body())
                .build()
        }
    }
}
```

## Building the application: Main activity
<a name="tutorial-maplibre-android-request-main-activity"></a>

The Main Activity is responsible for initializing the views that will be displayed to users. This involves:
+ Instantiating an Amazon Cognito `CredentialsProvider`.
+ Registering the Signature Version 4 interceptor.
+ Configuring the map by pointing it at a map style descriptor, and displaying appropriate attribution.

 `MainActivity` is also responsible for forwarding life cycle events to the map view, allowing it to preserve the active viewport between invocations.

```
package aws.location.demo.maplibre

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import aws.location.demo.okhttp.SigV4Interceptor
import com.amazonaws.auth.CognitoCachingCredentialsProvider
import com.amazonaws.regions.Regions
import com.mapbox.mapboxsdk.Mapbox
import com.mapbox.mapboxsdk.maps.MapView
import com.mapbox.mapboxsdk.maps.Style
import com.mapbox.mapboxsdk.module.http.HttpRequestUtil
import okhttp3.OkHttpClient

private const val SERVICE_NAME = "geo"

class MainActivity : AppCompatActivity() {
    private var mapView: MapView? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // configuration
        val identityPoolId = getString(R.string.identityPoolId)
        val region = getString(R.string.awsRegion)
        val mapName = getString(R.string.mapName)

        // Credential initialization
        val credentialProvider = CognitoCachingCredentialsProvider(
            applicationContext,
            identityPoolId,
            Regions.fromName(identityPoolId.split(":").first())
        )

        // initialize MapLibre
        Mapbox.getInstance(this, null)
        HttpRequestUtil.setOkHttpClient(
            OkHttpClient.Builder()
                .addInterceptor(SigV4Interceptor(credentialProvider, SERVICE_NAME))
                .build()
        )

        // initialize the view
        setContentView(R.layout.activity_main)

        // initialize the map view
        mapView = findViewById(R.id.mapView)
        mapView?.onCreate(savedInstanceState)
        mapView?.getMapAsync { map ->
            map.setStyle(
                Style.Builder()
                    .fromUri("https://maps.geo.${region}.amazonaws.com/maps/v0/maps/${mapName}/style-descriptor")
            ) { style ->
                findViewById<TextView>(R.id.attributionView).text = style.sources.first()?.attribution
            }
        }
    }

    override fun onStart() {
        super.onStart()
        mapView?.onStart()
    }

    override fun onResume() {
        super.onResume()
        mapView?.onResume()
    }

    override fun onPause() {
        super.onPause()
        mapView?.onPause()
    }

    override fun onStop() {
        super.onStop()
        mapView?.onStop()
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        mapView?.onSaveInstanceState(outState)
    }

    override fun onLowMemory() {
        super.onLowMemory()
        mapView?.onLowMemory()
    }

    override fun onDestroy() {
        super.onDestroy()
        mapView?.onDestroy()
    }
}
```

Running this application displays a full-screen map in the style of your choosing. This sample is available as part of the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

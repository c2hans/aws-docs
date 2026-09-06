---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-add-search-android.html
---

# Add Amazon Location reverse geocoding search to your application
<a name="qs-add-search-android"></a>

You will now add reverse geocoding search to your application, where you find the items at a location. To simplify using an Android app, we will search the center of the screen. To find a new location, move the map to where you want to search. We will place a marker at the centre of the map to show where we are searching.

Adding a reverse geocoding search will consist of two parts.
+ Add a marker at the centre of the screen to show the user where we are searching.
+ Add a text box for results, then search for what is at the marker's location and show it in the text box.

**To add a marker to your application**

1. Save this image to your project in the `app/res/drawable` folder as `red_marker.png` (you can also access the image from [GitHub](https://github.com/makeen-project/amazon-location-mobile-quickstart-android/tree/main/app/src/main/res/drawable). Alternatively, you can create your image. You can also use a .png file with transparency for the parts you don't want shown.

1. Add the following code to your **MapLoadScreen.kt** file.

   ```
   // ...other imports
   import androidx.compose.foundation.Image
   import androidx.compose.foundation.layout.size
   import androidx.compose.ui.Alignment
   import androidx.compose.ui.res.painterResource
   import androidx.compose.ui.unit.dp
   import com.amazon.testmapapp.R

   @Composable
   fun MapLoadScreen(
       mapReadyCallback: OnMapReadyCallback,
   ) {
       Box(
           modifier = Modifier
               .fillMaxWidth()
               .fillMaxHeight(),
       ) {
           MapView(mapReadyCallback)
           Box(
               modifier = Modifier
                   .align(Alignment.Center),
           ) {
               Image(
                   painter = painterResource(id = R.drawable.red_marker),
                   contentDescription = "marker",
                   modifier = Modifier
                       .size(40.dp)
                       .align(Alignment.Center),
               )
           }
       }
   }

   @Composable
   fun MapView(mapReadyCallback: OnMapReadyCallback) {
       AndroidView(
           factory = { context ->
               val mapView = org.maplibre.android.maps.MapView(context)
               mapView.onCreate(null)
               mapView.getMapAsync(mapReadyCallback)
               mapView
           },
       )
   }
   ```

1. Build and run your app to preview the functionality.

Your app now has a marker on the screen. In this case, it is a static image that doesn't move. It is used to show the centre of the map view, which is where we will search. In the following procedure, we will add the search at that location.

**To add reverse geocoding search at a location to your app**

1. In the **Project** window, open **gradle** to `libs.versions.toml` file in the tree view. This will open the `libs.versions.toml` file for editing. Now add the below version and libraries data in the `libs.versions.toml` file.

   ```
   [versions]
    ...
    okhttp = "4.12.0"

    [libraries]
    ...
    com-squareup-okhttp3 = { group = "com.squareup.okhttp3", name = "okhttp", version.ref = "okhttp" }

    [plugins]
    ...
   ```

1. After you finish editing the `libs.versions.toml` file, AndroidStudio must re-sync the project. At the top of the `libs.versions.toml` editing window, AndroidStudio prompts you to sync. Select 'Sync Now' to sync your project before continuing.

1. In the Project window, open Gradle Scripts in the tree view and select the `build.gradle` file for your application module. This will open the `build.gradle` file for editing.

1. At the bottom of the file, in the dependencies section, add the following dependency.

   ```
   dependencies {
       ...
       implementation(libs.com.squareup.okhttp3)
    }
   ```

1. After you finish editing the Gradle dependencies, AndroidStudio must re-sync the project. At the top of the `build.gradle` editing window, AndroidStudio prompts you to sync. Select **SyncNow** to sync your project before continuing.

1. Now in the tree view add the **data**, to the **request** directory, and create the `ReverseGeocodeRequest.kt` data class. Add the following code to the class.

   ```
   import com.google.gson.annotations.SerializedName

   data class ReverseGeocodeRequest(
       @SerializedName("Language")
       val language: String,
       @SerializedName("MaxResults")
       val maxResults: Int,
       @SerializedName("Position")
       val position: List{{Double}}
   )
   ```

1. Now in the tree view add the **data** to **response** directory, and create the `ReverseGeocodeResponse.kt` data class. Add the following code inside it.

   ```
   import com.google.gson.annotations.SerializedName

   data class ReverseGeocodeResponse(
       @SerializedName("Results")
       val results: List{{Result}}
   )

   data class Result(
       @SerializedName("Place")
       val place: Place
   )

   data class Place(
       @SerializedName("Label")
       val label: String
   )
   ```

1. Now, From the Project window, open App, Java, {{your package name}} in the tree view, and go to the **ui** folder, inside **ui** folder create **viewModel** directory.

1. Inside **viewModel** directory create `MainViewModel.kt` file.

1. Add the following code to your `MainViewModel.kt` file.

   ```
   import androidx.compose.runtime.getValue
   import androidx.compose.runtime.mutableStateOf
   import androidx.compose.runtime.setValue
   import androidx.lifecycle.ViewModel
   import com.amazon.testmapapp.data.request.ReverseGeocodeRequest
   import com.amazon.testmapapp.data.response.ReverseGeocodeResponse
   import com.google.gson.Gson
   import java.io.IOException
   import okhttp3.Call
   import okhttp3.Callback
   import okhttp3.MediaType.Companion.toMediaTypeOrNull
   import okhttp3.OkHttpClient
   import okhttp3.Request
   import okhttp3.RequestBody.Companion.toRequestBody
   import okhttp3.Response
   import org.maplibre.android.geometry.LatLng
   import org.maplibre.android.maps.MapLibreMap

   class MainViewModel : ViewModel() {
       var label by mutableStateOf("")
       var isLabelAdded: Boolean by mutableStateOf(false)
       var client = OkHttpClient()
       var mapLibreMap: MapLibreMap? = null

       fun reverseGeocode(latLng: LatLng, apiKey: String) {
           val region = "{{YOUR_AWS_REGION}}"
           val indexName = "{{YOUR_AWS_PLACE_INDEX}}"
           val url =
               "https://places.geo.${region}.amazonaws.com/places/v0/indexes/${indexName}/search/position?key=${apiKey}"

           val requestBody = ReverseGeocodeRequest(
               language = "en",
               maxResults = 1,
               position = listOf(latLng.longitude, latLng.latitude)
           )
           val json = Gson().toJson(requestBody)

           val mediaType = "application/json".toMediaTypeOrNull()
           val request = Request.Builder()
               .url(url)
               .post(json.toRequestBody(mediaType))
               .build()

           client.newCall(request).enqueue(object : Callback {
               override fun onFailure(call: Call, e: IOException) {
                   e.printStackTrace()
               }

               override fun onResponse(call: Call, response: Response) {
                   if (response.isSuccessful) {
                       val jsonResponse = response.body?.string()

                       val reverseGeocodeResponse =
                           Gson().fromJson(jsonResponse, ReverseGeocodeResponse::class.java)

                       val responseLabel = reverseGeocodeResponse.results.firstOrNull()?.place?.label

                       if (responseLabel != null) {
                           label = responseLabel
                           isLabelAdded = true
                       }
                   }
               }
           })
       }
   }
   ```

1. If it's not open already, open the `MapLoadScreen.kt` file, as in the previous procedure. Add the following code. This will create a compose Text view where you will see reverse geocoding search results at the location.

   ```
   // ...other imports
   import androidx.compose.foundation.background
   import androidx.compose.foundation.layout.Arrangement
   import androidx.compose.foundation.layout.Column
   import androidx.compose.foundation.layout.Spacer
   import androidx.compose.foundation.layout.fillMaxSize
   import androidx.compose.foundation.layout.height
   import androidx.compose.foundation.layout.padding
   import androidx.compose.material3.Text
   import androidx.compose.ui.graphics.Color
   import androidx.compose.ui.platform.testTag
   import androidx.compose.ui.semantics.contentDescription
   import androidx.compose.ui.semantics.semantics
   import androidx.compose.ui.unit.sp
   import com.amazon.testmapapp.ui.viewModel.MainViewModel

   @Composable
   fun MapLoadScreen(
       mapReadyCallback: OnMapReadyCallback,
       mainViewModel: MainViewModel,
   ) {
       Box(
           modifier = Modifier
               .fillMaxWidth()
               .fillMaxHeight(),
       ) {
           MapView(mapReadyCallback)
           Box(
               modifier = Modifier
                   .align(Alignment.Center),
           ) {
               Image(
                   painter = painterResource(id = R.drawable.red_marker),
                   contentDescription = "marker",
                   modifier = Modifier
                       .size(40.dp)
                       .align(Alignment.Center),
               )
           }
           if (mainViewModel.isLabelAdded) {
               Column(
                   modifier = Modifier.fillMaxSize(),
                   verticalArrangement = Arrangement.Bottom
               ) {
                   Box(
                       modifier = Modifier
                           .fillMaxWidth()
                           .background(Color.White),
                   ) {
                       Text(
                           text = mainViewModel.label,
                           modifier = Modifier
                               .padding(16.dp)
                               .align(Alignment.Center)
                               .testTag("label")
                               .semantics {
                                   contentDescription = "label"
                               },
                           fontSize = 14.sp,
                       )
                   }
                   Spacer(modifier = Modifier.height(80.dp))
               }
           }
       }
   }

   @Composable
   fun MapView(mapReadyCallback: OnMapReadyCallback) {
       AndroidView(
           factory = { context ->
               val mapView = org.maplibre.android.maps.MapView(context)
               mapView.onCreate(null)
               mapView.getMapAsync(mapReadyCallback)
               mapView
           },
       )
   }
   ```

1. In the app, under java, in the **package name** folder in AndroidStudio, open the `MainActivity.kt` file. Modify the code as shown.

   ```
   // ...other imports
   import androidx.activity.viewModels
   import com.amazon.testmapapp.ui.viewModel.MainViewModel

    class MainActivity : ComponentActivity(), OnMapReadyCallback, MapLibreMap.OnCameraMoveStartedListener, MapLibreMap.OnCameraIdleListener {

        private val mainViewModel: MainViewModel by viewModels()
        private val region = "{{YOUR_AWS_REGION}}"
        private val mapName = "{{YOUR_AWS_MAP_NAME}}"
        private val apiKey = "{{YOUR_AWS_API_KEY}}"
        override fun onCreate(savedInstanceState: Bundle?) {
            MapLibre.getInstance(this)
            super.onCreate(savedInstanceState)
            setContent {
                TestMapAppTheme {
                    Surface(
                        modifier = Modifier.fillMaxSize(),
                        color = MaterialTheme.colorScheme.background
                    ) {
                        MapLoadScreen(this, mainViewModel)
                    }
                }
            }
        }

        override fun onMapReady(map: MapLibreMap) {
            map.setStyle(
                Style.Builder()
                    .fromUri(
                        "https://maps.geo.$region.amazonaws.com/maps/v0/maps/$mapName/style-descriptor?key=$apiKey"
                    ),
            ) {
                map.uiSettings.isAttributionEnabled = true
                map.uiSettings.isLogoEnabled = false
                map.uiSettings.attributionGravity = Gravity.BOTTOM or Gravity.END
                val initialPosition = LatLng(47.6160281982247, -122.32642111977668)
                map.cameraPosition = CameraPosition.Builder()
                    .target(initialPosition)
                    .zoom(14.0)
                    .build()

                map.addOnCameraMoveStartedListener(this)
                map.addOnCameraIdleListener(this)
                map.cameraPosition.target?.let { latLng ->
                    mainViewModel.reverseGeocode(
                        LatLng(
                            latLng.latitude,
                            latLng.longitude
                        ), apiKey
                    )
                }
            }
        }
       override fun onCameraMoveStarted(p0: Int) {
           mainViewModel.label = ""
           mainViewModel.isLabelAdded = false
       }

       override fun onCameraIdle() {
           if (!mainViewModel.isLabelAdded) {
               mainViewModel.mapLibreMap?.cameraPosition?.target?.let { latLng ->
                   mainViewModel.reverseGeocode(
                       LatLng(
                           latLng.latitude,
                           latLng.longitude
                       ), apiKey
                   )
               }
           }
       }
    }
   ```

   This code works with the map view. A virtual camera position defines the map view in MapLibre. Moving the map can be thought of as moving that virtual camera.
   + ViewModel has a label variable: This variable sets data in compose text view.
   + **onMapReady**:This function is updated to register two new events.
   + The **onCameraMove** event happens whenever the user is moving the map. In general, when moving the map, we want to hide the search until the user is done moving the map.
   + The **onCameraIdle** event occurs when the user pauses moving the map. This event calls our reverse geocode function to search at the centre of the map.
   + `reverseGeocode(latLng: LatLng, apiKey: String)`: This function, called in the event onCameraIdle, searches at the centre of the map for a location and updates the label to show the results. It uses the camera target, which defines the centre of the map (where the camera is looking).

1. Save your files, and build and run your app to see if it works.

Your quick-start application with search functionality is complete.

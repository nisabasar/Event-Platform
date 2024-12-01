<template>
    <div id="map" style="width: 100%; height: 400px;"></div>
  </template>
  
  <script>
  export default {
    props: {
      location: {
        type: String,
        required: true,
      },
    },
    data() {
      return {
        map: null,
        marker: null,
      };
    },
    mounted() {
      this.initMap();
    },
    methods: {
      initMap() {
        // Geocoding API ile konumu coğrafi koordinatlara çevir
        const geocoder = new google.maps.Geocoder();
        geocoder.geocode({ address: this.location }, (results, status) => {
          if (status === "OK") {
            const mapOptions = {
              center: results[0].geometry.location,
              zoom: 14,
            };
            this.map = new google.maps.Map(
              document.getElementById("map"),
              mapOptions
            );
            this.marker = new google.maps.Marker({
              position: results[0].geometry.location,
              map: this.map,
            });
          } else {
            console.error("Harita yüklenirken hata oluştu:", status);
          }
        });
      },
    },
  };
  </script>
  
  <style>
  #map {
    border-radius: 8px;
    overflow: hidden;
  }
  </style>
  
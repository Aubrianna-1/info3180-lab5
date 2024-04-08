<template>
<h1 class="heading">Movies</h1>
<ul class="img-grid">
    <li v-for="m in movies">
        <div class="movie_card">
            <img :src= "m.poster"  alt="Movie poster">
            <div class="info">
                <h3>{{ m.title }}</h3>
                <p>{{ m.description }}</p>
            </div>
        </div>
    </li>
</ul>
      
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);
onMounted(() => {
  fetchMovies();
});

function fetchmovies(){
   
   fetch("/api/v1/movies", {
     method:'GET'
   })
         .then((response) => response.json())
         .then((data) => {
                movies.value = data.Movies;
                console.log(movies.value);
         })
         .catch(function (error) {
              console.log(error);
          });
}
</script>




<template>
   <div class="home">
      <TopNav class="TopNav" />
      <div class="main-layout">
         <LeftNav style="height: 100%;" />
         <router-view class="body" />
      </div>
   </div>
</template>

<script>
import TopNav from '../components/Topnav.vue';
import LeftNav from '../components/LeftNav.vue';
// import PageContent from '../components/PageContent.vue';

export default {
   name: 'home',
   components: {
      TopNav,
      LeftNav,
      // PageContent
   }
};
</script>

<style>
.home {
   font-family: Avenir, Helvetica, Arial, sans-serif;
   -webkit-font-smoothing: antialiased;
   -moz-osx-font-smoothing: grayscale;
   text-align: center;
   color: #2c3e50;
}

.TopNav {
   height: 100px;
}

.main-layout {
   display: flex;
   height: calc(100vh - 100px);
}

.body {
   flex: 1;
   background-color: #faf3f3;
   /* background-image: url(../assets/preview-0002.jpg); */
}
</style>
<template>
    <b-container>
        <b-row>
            <b-col>
                <h1>Bienvenido Gonzalo a tu primera aplicación Vue </h1>
                <img src="../assets/Logo.jpg" alt="" width ="30%" height="auto" rounded="circle">
            </b-col>
        </b-row>
        <b-row >
            <b-col v-for="red in redes" :key="red.red" class="text-center">
                <b-link :href="red.url" target = "_blank">
                    <b-alert :variant="red.color" show>
                            {{red.red}} 
                    </b-alert>    
                </b-link>
            </b-col>
        </b-row>    
    </b-container>
</template>

<script>


export default {
  name: 'Home',
  data(){
      return{
          redes:[
              {
                  red:"Mi Facebook1",
                  url:"https://www.facebook.com/gibarramendoza/",
                  color:"info"
              },
                {
                  red:"Mi Facebook2",
                  url:"https://www.facebook.com/gibarramendoza/",
                  color:"warning"
              },
              {
                  red:"Mi Facebook3",
                  url:"https://www.facebook.com/gibarramendoza/",
                  color:"danger"
              }
          ]
      }
    
  }
}
</script>

<style lang="stylus" scoped>

</style>
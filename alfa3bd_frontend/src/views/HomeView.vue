<script setup lang="ts">
</script>

<template>
  <main>
    <label for="language">Select a Programming Language:</label>
    <select name="language" id="language">
      <option value="javascript">JavaScript</option>
      <option value="python">Python</option>
      <option value="c++" disabled>C++</option>
      <option value="java" selected>Java</option>
    </select>
  </main>
</template>


<style>

body{
  background: #0a0a23;
  min-height:100vh;
  display:flex;
  justify-content:center;
  align-items:center;
  color:#fff;
}

select{
  border:none;
  padding: 10px 20px;
  border-radius:5px;
}

select:focus{
  outline:none;
}

</style>
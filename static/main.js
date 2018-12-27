$(document).ready(function(){
app = new Vue({
  el: '#app',
  delimiters: ["{(",")}"],
  data: {
    content: 'Can I go to the mall?',
    cleanedContent: '',
  },
  created: function() {
    $.post('/clean_content', {'content': this.content}, function(data) {
    app.cleanedContent = data.cleaned_content;
    })
  },
  methods: {
    cleanContent: function() {
      $.post('/clean_content', {'content': this.content}, function(data) {
      app.cleanedContent = data.cleaned_content;
      })
    },
    runContent: function(content) {
      this.content = content;
      this.cleanContent();
    }
  }
})
});

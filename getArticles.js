/*
 * Auth: Taylor Walenczyk
 * Date Created: 10/13/2017
 * Last Updated: 10/13/2017
 */

// Maybe some that loads on page load
var nyt_url = "https://query.nytimes.com/search/sitesearch/?action=click&contentCollection&region=TopBar&WT.nav=searchWidget&module=SearchSubmit&pgtype=Homepage#/"

var submit = function() {
    let topic = document.getElementById("topic").value
    let articles = getArticles(topic)
}

// Takes in a topic and finds relevant articles based on headlines
var getArticles = function(topic) {
    // go to a site
    // get a list of articles
    // filter based on title
    // return filtered list
    let topicURL = nyt_url + topic.replace(' ', '%20')


    // navigate to the page
    let nytWindow = window.open(topicURL)
    // get a list of headlines and urls
    let titles = []
    nytWindow.onload = function() {
        // get a list of headlines and urls
        let stories = document.getElementsByClassName("story")
        stories.foreach((story) => {
            titles.push(story.getElementsByTagName("h3"))
        })
    }

}

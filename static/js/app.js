// Read embed URL from textbox
var embedUrl = "https://app.powerbi.com/dashboardEmbed?dashboardId=" + dashboardId;
  
// Get models. models contains enums that can be used.
var models = window['powerbi-client'].models;
 
// Embed configuration used to describe the what and how to embed.
// This object is used when calling powerbi.embed.
// This also includes settings and options such as filters.
// You can find more information at https://github.com/Microsoft/PowerBI-JavaScript/wiki/Embed-Configuration-Details.
var config = {
    type: 'dashboard',
    tokenType: models.TokenType.Aad,
    accessToken: accessToken,
    embedUrl: embedUrl,
    id: dashboardId
};
 
// Get a reference to the embedded dashboard HTML element
var dashboardContainer = $('#dashboardContainer')[0];
 
// Embed the dashboard and display it within the div container.
var dashboard = powerbi.embed(dashboardContainer, config);
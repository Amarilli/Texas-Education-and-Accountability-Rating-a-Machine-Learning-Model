document.addEventListener('DOMContentLoaded', function() {
    fetchDataAndUpdateVisualization();

    function fetchDataAndUpdateVisualization() {
        fetch('/datadistrict')  // Adjust this endpoint as needed
            .then(response => response.json())
            .then(data => {
                console.log(data);  // Check what the data looks like
                updateVisualization(data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }

    function updateVisualization(data) {
        const margin = { top: 20, right: 30, bottom: 40, left: 90 },
              width = 960 - margin.left - margin.right,
              height = 500 - margin.top - margin.bottom;

        const svg = d3.select('#visualization').append('svg')
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom)
          .append('g')
            .attr('transform',
                  'translate(' + margin.left + ',' + margin.top + ')');

        // X scale and Axis
        const x = d3.scaleLinear()
            .domain([0, 100])
            .range([0, width]);

        svg.append('g')
            .attr('transform', 'translate(0,' + height + ')')
            .call(d3.axisBottom(x))
            .selectAll('text')
            .style('text-anchor', 'end');

        // Y scale and Axis
        const y = d3.scaleBand()
            .range([0, height])
            .domain(data.map(function(d) { return d.subject; }))
            .padding(.1);
        
        svg.append('g')
            .call(d3.axisLeft(y));

        // Bars
        svg.selectAll('myRect')
            .data(data)
            .enter()
            .append('rect')
            .attr('x', x(0))
            .attr('y', d => y(d.subject))
            .attr('width', d => x(d.score))
            .attr('height', y.bandwidth())
            .attr('fill', '#69b3a2');
    }
});

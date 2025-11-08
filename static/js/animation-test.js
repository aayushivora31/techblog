// Animation performance test
console.log('Animation test loaded');

// Performance monitoring
let animationFrameCount = 0;
let lastTime = performance.now();

function monitorPerformance() {
    animationFrameCount++;
    const currentTime = performance.now();
    
    if (currentTime - lastTime >= 1000) { // Every second
        console.log(`Animation frames per second: ${animationFrameCount}`);
        animationFrameCount = 0;
        lastTime = currentTime;
    }
    
    requestAnimationFrame(monitorPerformance);
}

// Start monitoring
requestAnimationFrame(monitorPerformance);
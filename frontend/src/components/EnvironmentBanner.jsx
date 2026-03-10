function EnvironmentBanner() {
    const env = import.meta.env.VITE_ENVIRONMENT;
  
    if (env === "PRODUCTION") return null;
  
    const colors = {
      LOCAL: "#dc3545",
      STAGING: "#ffcc00"
    };
  
    const backgroundColor = colors[env] || "#999";
  
    return (
      <div
        style={{
          position: "fixed",
          top: 0,
          left: 0,
          width: "100%",
          backgroundColor,
          color: env === "STAGING" ? "#000" : "#fff",
          textAlign: "center",
          padding: "6px",
          fontWeight: "bold",
          zIndex: 9999
        }}
      >
        {env} ENVIRONMENT
      </div>
    );
  }
  
  export default EnvironmentBanner;
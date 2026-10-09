
import { useState } from "react";

const categories = [
  "All Categories",
  "Music",
  "Tech",
  "Sports",
  "Business",
];

export default function Events() {
  const [selectedCategory, setSelectedCategory] =
    useState("All Categories");

  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundColor: "#f3f4f6",
        fontFamily: "Arial, sans-serif",
      }}
    >
      {/* Header */}
      <header
        style={{
          backgroundColor: "#ffffff",
          padding: "24px 40px",
          boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
        }}
      >
        <h1
          style={{
            color: "#4f46e5",
            fontSize: "32px",
            margin: 0,
          }}
        >
          SmartEvent
        </h1>

        <p style={{ color: "#6b7280", marginBottom: 0 }}>
          Discover events and book your tickets
        </p>
      </header>

      {/* Main Content */}
      <main style={{ maxWidth: "1100px", margin: "0 auto", padding: "32px 24px" }}>
        <h2 style={{ color: "#1f2937", marginBottom: "24px" }}>
          Explore Events
        </h2>

        {/* Category Buttons */}
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: "12px",
            alignItems: "center",
          }}
        >
          {categories.map((category) => (
            <button
              key={category}
              type="button"
              onClick={() => setSelectedCategory(category)}
              style={{
                padding: "12px 20px",
                borderRadius: "24px",
                border:
                  selectedCategory === category
                    ? "1px solid #4f46e5"
                    : "1px solid #d1d5db",
                backgroundColor:
                  selectedCategory === category
                    ? "#4f46e5"
                    : "#ffffff",
                color:
                  selectedCategory === category
                    ? "#ffffff"
                    : "#374151",
                cursor: "pointer",
                fontSize: "14px",
                fontWeight: "600",
              }}
            >
              {category}
            </button>
          ))}
        </div>

        {/* Selected Category */}
        <section
          style={{
            marginTop: "32px",
            padding: "28px",
            backgroundColor: "#ffffff",
            border: "1px solid #e5e7eb",
            borderRadius: "12px",
          }}
        >
          <h3 style={{ color: "#1f2937", marginTop: 0 }}>
            {selectedCategory === "All Categories"
              ? "All Events"
              : `${selectedCategory} Events`}
          </h3>

          <p style={{ color: "#6b7280", marginBottom: 0 }}>
            {selectedCategory === "All Categories"
              ? "Explore all available events."
              : `Explore events in the ${selectedCategory} category.`}
          </p>
        </section>
      </main>
    </div>
  );
}

